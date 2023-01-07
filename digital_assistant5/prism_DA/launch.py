import random
import json
import glob, os
import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

from email import message
from urllib import response
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from quest_ans import bell

intents = bell

from py4j.java_gateway import JavaGateway
gateway = JavaGateway()                 
prism_java = gateway.entry_point   

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]
result = {}


model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Combot"

app = Flask(__name__)
CORS(app)


yes="yes"
no="no"

@app.get("/")
def index_get():
    return render_template("basen.html")

@app.post("/upload_static_file")
def upload_static_file():
 print("Got request in static files")
 print(request.files)
 f = request.files['static_file']
 f.save(f.filename)
 print(f.filename)
 resp = {"success": True, "response": "file saved!"}
 return jsonify(resp), 200


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    sentence = tokenize(text)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    if tag == "level":
        result["operation"] = "level"

    if tag == "one_two":
        result["operation1"] = "one_two"

    if tag == "one_three":
        result["operation2"] = "one_three"

    if tag == "three_two":
        result["operation3"] = "three_two"

    if tag == "three_three":
        result["operation4"] = "three_three"


    if (len(glob.glob("*.txt")) or len(glob.glob("*.prism"))) != 0:
        cwd = os.getcwd()
        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
        ret = max(text_files, key=os.path.getctime)
        filename_MDP, file_extension = os.path.splitext(ret)
        proz12 = prism_java.five_three(filename_MDP, file_extension)
        a = proz12
        b = "[]"
        for char in b:
            a = a.replace(char, "")
        arr = a.split(', ')
        print(arr)
    else:
        respond2 = "Error, MDP Model (.txt or .prism) file does not exist! Please upload your MDP Model file."
        message2 = {"answer": respond2}
        return (jsonify(message2))


    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:


                if tag == "one_one":
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)
                        filename_MDP, file_extension = os.path.splitext(ret)

                        with open(ret) as f:

                            if "label \"end_state\"" in f.read():
                                
                                with open('pwd.text', 'r') as file :
                                    filedata = file.read()
                                # Write the file out again
                                nm='mdp.pctl'
                                with open(nm, 'w') as file:
                                    file.write(filedata)

                                filename_properties, file_extension1 = os.path.splitext(nm)

                                probabs11 = prism_java.one_one(filename_MDP, file_extension, filename_properties)
                                probap11=format(probabs11*100, ".2f")                       

                                ans1 = {"answer": f"GP 2.1.3 and GP 2.1.7 are satisfied because we have no deadlocks in the process. The probability of reaching the final state is {probap11}%. All interfaces are managed well."}
                                ans2 = {"answer": f"GP 2.1.3 and GP 2.1.7 are unfortunately not satisfied because we have deadlocks in the process. The probability of reaching the final state is {probap11}%. All interfaces are not managed well."}

                                if probabs11 == 1.0:
                                    return (jsonify(ans1))
                                else:
                                    return (jsonify(ans2))
                                    
                            else:

                                list_of_lists = []
                                res= []

                                with open(ret) as file_in:
                                    lines = []
                                    for line in file_in:
                                        lines.append(line)
                                grant= [i for i in range(len(lines)) if lines[i].startswith('endmodule')]

                                for i in range(len(grant)):
                                    grant[i] = grant[i] - 1

                                for i in range(len(grant)):
                                    if lines[grant[i]]=='\n':
                                        del lines[grant[i]]

                                textfile = open("a_file.txt", "w")
                                for element in lines:
                                    textfile.write(element)
                                textfile.close()

                                with open("a_file.txt") as f:
                                    line = ''
                                    for next_line in f:
                                        if next_line.startswith('endmodule'):
                                            val = line.split('(', 1)[1].split(')')[0]
                                            val1=val.replace("\'", "")
                                            list_of_lists.append('('+val1+')')
                                        line = next_line

                                s= ' & '.join(list_of_lists)
                                stran="label \"end_state\" = "+s+";"

                                with open(ret, "a+") as file_object:
                                    # Move read cursor to the start of file.
                                    file_object.seek(0)
                                    # If file is not empty then append '\n'
                                    data = file_object.read(100)
                                    if len(data) > 0 :
                                        file_object.write("\n")
                                    # Append text at the end of file
                                    file_object.write('\n'+stran)

                                # Read in the file
                                with open('pwd.text', 'r') as file :
                                    filedata = file.read()

                                # Write the file out again
                                nm='mdp.pctl'
                                with open(nm, 'w') as file:
                                    file.write(filedata)

                                filename_properties12, file_extension1 = os.path.splitext(nm)

                                probabs11 = prism_java.one_one(filename_MDP, file_extension, filename_properties12)
                                probap11=format(probabs11*100, ".2f")                       

                                ans1 = {"answer": f"GP 2.1.3 and GP 2.1.7 are satisfied because we have no deadlocks in the process. The probability of reaching the final state is {probap11}%. All interfaces are managed well."}
                                ans2 = {"answer": f"GP 2.1.3 and GP 2.1.7 are unfortunately not satisfied because we have deadlocks in the process. The probability of reaching the final state is {probap11}%. All interfaces are not managed well."}

                                if probabs11 == 1.0:
                                    return (jsonify(ans1))
                                else:
                                    return (jsonify(ans1))
                           

                if "number_one" not in result.keys() and (text.casefold() in arr):
                    if 'operation1' in result.keys() and (text.casefold() in arr):
                        result["number_one"] = text.casefold()
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)
                        filename_MDP, file_extension = os.path.splitext(ret)
                    
                        list_of_lists = []
                        res= []
                        with open(ret, "r") as file:
                            for line in file:
                                s = line.strip()
                                search_word = "("
                                if s.startswith("label"):
                                    if(search_word in s):
                                        qer=s.split("(")[0]
                                        usr = s.replace(qer, "")
                                        list_of_lists.append(usr)
                                else:
                                    list_of_lists.append(s)

                        for i in list_of_lists:
                            if i:
                                res.append(i)

                        indices1 = [i for i, sv in enumerate(res) if '(' in sv]
                        indices2 = [i for i, sv in enumerate(res) if ';' in sv]

                        if indices2[0]>=indices1[0]:
                                ax=res[int(indices1[0]):int(indices2[0]+1)]

                        rew=[]
                        rew.append(" ".join(ax))
                        st=rew[0]
                        usry = st.replace(";","")
                        print("Pmin ? = [F",str(usry),"]")
                        
                        qjr=usry.split(text.casefold())[1]
                        qjq=qjr.split("=")[1]
                        if qjq.startswith((' ', '\t')):
                            qjq=qjq.strip()

                        faz=qjq.split(")")[0]
                        print(faz)

                        with open('pwd.text', 'r') as file :
                            filedata = file.read()
                        filedata = filedata.replace("pax",text.casefold())
                        filedata = filedata.replace("cax",faz)

                        with open('mdp.pctl', 'w') as file:
                            file.write(filedata)

                        with open('mdp.pctl', 'r') as fin:
                            data = fin.read().splitlines(True)
                        with open('mdp.pctl', 'w') as fout:
                            fout.writelines(data[2:])
                        nm='mdp.pctl'

                        filename_properties, file_extension1 = os.path.splitext(nm)

                        probabs12 = prism_java.one_two(filename_MDP, file_extension, filename_properties)
                        probap12=format(probabs12*100, ".2f")                       

                        ans1 = {"answer": f"The probability of P=? [F {text.casefold()} = {faz}] reaching the final state of the process is: {probap12}%. There are no deadlocks and therefore, the final state can always be reached and proves the compliance with A-SPICE Level 2 of GP 2.1.3 and GP 2.1.7"}
                        ans2 = {"answer": f"The probability of P=? [F {text.casefold()} = {faz}] reaching the final state of the process is: {probap12}%. Unfortunately, there are deadlocks and the final state cannot be reached. The A-SPICE Level 2 of GP 2.1.3 and GP 2.1.7 are not complied."}

                        del result['operation1']
                        del result['number_one']
                        
                        if probabs12 == 1.0:
                            return (jsonify(ans1))
                        else:
                            return (jsonify(ans2))


                if "numbza" not in result.keys() and (text.casefold() in arr):
                    if 'operation2' in result.keys() and (text.casefold() in arr):
                        result["numbza"] = text.casefold()
                        respond2 = "Please enter the state number: "
                        message2 = {"answer": respond2}
                        return (jsonify(message2))
                    

                if 'operation2' and "numbza" in result.keys():
                    if result["operation2"] == "one_three" and (isinstance(int(text), int) or isinstance(float(text), float)):

                        zen=result["numbza"]
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)

                        filename_MDP, file_extension = os.path.splitext(ret)

                    # Read in the file
                        with open('pwd2.text', 'r') as file :
                            filedata = file.read()
                        filedata = filedata.replace("tax",zen)
                        filedata = filedata.replace("wax",text)

                        with open('mdp.pctl', 'w') as file:
                            file.write(filedata)

                        with open('mdp.pctl', 'r') as fin:
                            data = fin.read().splitlines(True)
                        with open('mdp.pctl', 'w') as fout:
                            fout.writelines(data[2:])
                        nm='mdp.pctl'

                        filename_properties, file_extension1 = os.path.splitext(nm)

                        probabs = prism_java.one_three(filename_MDP, file_extension, filename_properties)

                        probap=format(probabs*100, ".2f")                       

                        ans1 = {"answer": f"The probability of P=? [F {zen} = {text}] reaching the final state of the process is: {probap}%. There are no deadlocks and therefore, the final state can always be reached and proves the compliance with A-SPICE Level 2 of GP 2.1.3 and GP 2.1.7"}
                        ans2 = {"answer": f"The probability of P=? [F {zen} = {text}] reaching the final state of the process is: {probap}%. Unfortunately, there are deadlocks and the final state cannot be reached. The A-SPICE Level 2 of GP 2.1.3 and GP 2.1.7 are not complied."}

                        del result['operation2']
                        del result['numbza']

                        if probabs == 1.0:
                            return (jsonify(ans1))
                        else:
                            return (jsonify(ans2))

                    else:
                        message2 = {"answer": "Error, please enter a valid state number"}
                        return (jsonify(message2))

                if tag == "two_one":
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)

                        filename_MDP, file_extension = os.path.splitext(ret)

                        try:
                            probabs21 = prism_java.two_one(filename_MDP, file_extension)
                            probap11=format(probabs21, ".2f")
                            ans1 = {"answer": f"The minimum days for performing whole process is {probap11} days."}
                            return (jsonify(ans1))
                        except:
                            ans1 = {"answer": f"Error: Model has no rewards specified."}
                            return (jsonify(ans1))
                        

                if tag == "three_one":
                    cwd = os.getcwd()
                    text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                    ret = max(text_files, key=os.path.getctime)
                    filename_MDP, file_extension = os.path.splitext(ret)

                    with open(ret) as f:

                        if "label \"end_state\"" in f.read():
                            
                            with open('pwd.text', 'r') as file :
                                filedata = file.read()
                            # Write the file out again
                            nm='mdp.pctl'
                            with open(nm, 'w') as file:
                                file.write(filedata)

                            filename_properties, file_extension1 = os.path.splitext(nm)
                            try:
                                probabs31 = prism_java.three_one(filename_MDP, file_extension, filename_properties)
                                probap13=format(probabs31, ".2f")                       

                                ans1 = {"answer": f"The estimation of expected minimum days for performing whole process is {probap13} days."}
                                return (jsonify(ans1))
                            except:
                                ans1 = {"answer": f"Error: Model has no rewards specified. Please perform ‘make test’ again on terminal and rerun the program to restart the digital assistant."}
                                return (jsonify(ans1))
                                
                        else:

                            list_of_lists = []
                            res= []

                            with open(ret) as file_in:
                                lines = []
                                for line in file_in:
                                    lines.append(line)
                            grant= [i for i in range(len(lines)) if lines[i].startswith('endmodule')]

                            for i in range(len(grant)):
                                grant[i] = grant[i] - 1

                            for i in range(len(grant)):
                                if lines[grant[i]]=='\n':
                                    del lines[grant[i]]

                            textfile = open("a_file.txt", "w")
                            for element in lines:
                                textfile.write(element)
                            textfile.close()

                            with open("a_file.txt") as f:
                                line = ''
                                for next_line in f:
                                    if next_line.startswith('endmodule'):
                                        val = line.split('(', 1)[1].split(')')[0]
                                        val1=val.replace("\'", "")
                                        list_of_lists.append('('+val1+')')
                                    line = next_line

                            s= ' & '.join(list_of_lists)
                            stran="label \"end_state\" = "+s+";"

                            with open(ret, "a+") as file_object:
                                # Move read cursor to the start of file.
                                file_object.seek(0)
                                # If file is not empty then append '\n'
                                data = file_object.read(100)
                                if len(data) > 0 :
                                    file_object.write("\n")
                                # Append text at the end of file
                                file_object.write('\n'+stran)

                                # Read in the file
                            with open('pwd.text', 'r') as file :
                                filedata = file.read()
                            # Replace the target string
                                # filedata = filedata.replace('q', str("pand"))

                            # Write the file out again
                            nm='mdp.pctl'
                            with open(nm, 'w') as file:
                                file.write(filedata)

                            filename_properties, file_extension1 = os.path.splitext(nm)
                            try:
                                probabs31 = prism_java.three_one(filename_MDP, file_extension, filename_properties)
                                probap13=format(probabs31, ".2f")                       

                                ans1 = {"answer": f"The estimation of expected minimum days for performing whole process is {probap13} days."}
                                return (jsonify(ans1))
                            except:
                                ans1 = {"answer": f"Error: Model has no rewards specified. Please perform ‘make test’ again on terminal and rerun the program to restart the digital assistant."}
                                return (jsonify(ans1))

                if "number_three" not in result.keys() and (text.casefold() in arr):
                    if 'operation3' in result.keys() and (text.casefold() in arr):
                        result["number_three"] = text.casefold()
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)

                        filename_MDP, file_extension = os.path.splitext(ret)
                    
                        list_of_lists = []
                        res= []
                        with open(ret, "r") as file:
                            for line in file:
                                s = line.strip()
                                search_word = "("
                                if s.startswith("label"):
                                    if(search_word in s):
                                        qer=s.split("(")[0]
                                        usr = s.replace(qer, "")
                                        list_of_lists.append(usr)
                                else:
                                    list_of_lists.append(s)

                        for i in list_of_lists:
                            if i:
                                res.append(i)

                        indices1 = [i for i, sv in enumerate(res) if '(' in sv]
                        indices2 = [i for i, sv in enumerate(res) if ';' in sv]

                        if indices2[0]>=indices1[0]:
                                ax=res[int(indices1[0]):int(indices2[0]+1)]

                        rew=[]
                        rew.append(" ".join(ax))
                        st=rew[0]
                        usry = st.replace(";","")
                        print("Pmin ? = [F",str(usry),"]")
                        
                        qjr=usry.split(text.casefold())[1]
                        qjq=qjr.split("=")[1]
                        if qjq.startswith((' ', '\t')):
                            qjq=qjq.strip()

                        faz=qjq.split(")")[0]
                        print(faz)

                        with open('pwd.text', 'r') as file :
                            filedata = file.read()
                        filedata = filedata.replace("pax",text.casefold())
                        filedata = filedata.replace("cax",faz)

                        with open('mdp.pctl', 'w') as file:
                            file.write(filedata)

                        with open('mdp.pctl', 'r') as fin:
                            data = fin.read().splitlines(True)
                        with open('mdp.pctl', 'w') as fout:
                            fout.writelines(data[2:])
                        nm='mdp.pctl'

                        filename_properties, file_extension1 = os.path.splitext(nm)
                        try:
                            probabs12 = prism_java.three_two(filename_MDP, file_extension, filename_properties)                
                            probap11=format(probabs12, ".2f")                       

                            ans1 = {"answer": f"The estimation of expected minimum days for variable {text.casefold()} to reach final state is {probap11} days."}

                            del result['operation3']
                            del result['number_three']

                            return (jsonify(ans1))
                        except:
                            ans1 = {"answer": f"Error: Model has no rewards specified. Please perform ‘make test’ again on terminal and rerun the program to restart the digital assistant."}
                            return (jsonify(ans1))


                if "numbzar" not in result.keys() and (text.casefold() in arr):
                    if 'operation4' in result.keys() and (text.casefold() in arr):
                        result["numbzar"] = text.casefold()
                        respond2 = "Please enter the state number: "
                        message2 = {"answer": respond2}
                        return (jsonify(message2))
                    

                if 'operation4' and "numbzar" in result.keys():
                    if result["operation4"] == "three_three" and (isinstance(int(text), int) or isinstance(float(text), float)):
     
                        zen=result["numbzar"]
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)

                        filename_MDP, file_extension = os.path.splitext(ret)

                    # Read in the file
                        with open('pwd2.text', 'r') as file :
                            filedata = file.read()
                        filedata = filedata.replace("tax",zen)
                        filedata = filedata.replace("wax",text)

                        with open('mdp.pctl', 'w') as file:
                            file.write(filedata)

                        with open('mdp.pctl', 'r') as fin:
                            data = fin.read().splitlines(True)
                        with open('mdp.pctl', 'w') as fout:
                            fout.writelines(data[2:])
                        nm='mdp.pctl'

                        filename_properties, file_extension1 = os.path.splitext(nm)
                        try:
                            probabs = prism_java.three_three(filename_MDP, file_extension, filename_properties)                       
                            probap11=format(probabs, ".2f")                       

                            ans1 = {"answer": f"The estimation of expected minimum days for variable {zen} to reach state {text} is {probap11} days."}

                            del result['operation4']
                            del result['numbzar']

                            return (jsonify(ans1))
                        except:
                            ans1 = {"answer": f"Error: Model has no rewards specified. Please perform ‘make test’ again on terminal and rerun the program to restart the digital assistant."}
                            return (jsonify(ans1))
                    else:
                        message2 = {"answer": "Error, please enter a valid state number"}
                        return (jsonify(message2))

                if tag == "four_one":
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)
                        filename_MDP, file_extension = os.path.splitext(ret)

                        probabs41 = prism_java.four_one(filename_MDP, file_extension)
                        ans1 = {"answer": f"The total number of transitions of the processes is {probabs41}."}
                        return (jsonify(ans1))


                if tag == "four_two":
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)
                        filename_MDP, file_extension = os.path.splitext(ret)

                        probabs42 = prism_java.four_two(filename_MDP, file_extension)
                        ans1 = {"answer": f"The total number of states of the processes is {probabs42}."}
                        return (jsonify(ans1))


                if tag == "four_three":
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)
                        filename_MDP, file_extension = os.path.splitext(ret)

                        probabs43 = prism_java.four_three(filename_MDP, file_extension)
                        ans1 = {"answer": f"The value of initial state of the processes is {probabs43}."}
                        return (jsonify(ans1))


                if tag == "four_four":
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)
                        filename_MDP, file_extension = os.path.splitext(ret)

                        probabs44 = prism_java.four_four(filename_MDP, file_extension)
                        ans1 = {"answer": f"Time for model construction is {probabs44/ 1000.0} seconds."}
                        return (jsonify(ans1))


                if tag == "five_one":
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)

                        filename_MDP, file_extension = os.path.splitext(ret)

                        with open('pwd.text', 'r') as file :
                            filedata = file.read()

                        nm='mdp.pctl'
                        with open(nm, 'w') as file:
                            file.write(filedata)

                        filename_properties, file_extension1 = os.path.splitext(nm)
                        probabs51 = prism_java.five_one(filename_MDP, file_extension, filename_properties)
                        ans1 = {"answer": f"Time for model checking is {probabs51/ 1000.0} seconds."}
                        return (jsonify(ans1))


                if tag == "five_two":
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)
                        filename_MDP, file_extension = os.path.splitext(ret)

                        probabs52 = prism_java.five_two(filename_MDP, file_extension)
                        ans1 = {"answer": f"The names of the modules are {probabs52}."}
                        return (jsonify(ans1))


                if tag == "five_three":
                        cwd = os.getcwd()
                        text_files =[_ for _ in os.listdir(cwd) if _.endswith('.txt') or _.endswith('.prism')]
                        ret = max(text_files, key=os.path.getctime)
                        filename_MDP, file_extension = os.path.splitext(ret)

                        probabs53 = prism_java.five_three(filename_MDP, file_extension)
                        ans1 = {"answer": f"The names of the variables are {probabs53}."}
                        return (jsonify(ans1))


                if "ones" not in result.keys() and (text.casefold() == yes or text.casefold() == no):
                    if 'operation' in result.keys() and (text.casefold() == yes):
                        result["ones"] = text
                        respond2 = "GP 2.1.1 Identify the objectives for the performance of the process<br/><br/>GP 2.1.2 Plan the performance of the process to fulfill the identified objectives<br/><br/>GP 2.1.3 Monitor the performance of the process against the plans<br/><br/>GP 2.1.4 Adjust the performance of the process<br/><br/>GP 2.1.5 Define responsibilities and authorities for performing the process<br/><br/>GP 2.1.6 Identify, prepare and make available resources to perform the process according to plan<br/><br/>GP 2.1.7 Manage the interfaces between involved parties<br/><br/>GP 2.2.1 Define the requirements for the work products<br/><br/>GP 2.2.2 Define the requirements for documentation and control of the work products<br/><br/>GP 2.2.3 Identify, document and control the work products<br/><br/>GP 2.2.4 Review and adjust work products to meet the defined requirement"
                        message2 = {"answer": respond2}
                        del result['ones']
                        del result['operation']
                        return (jsonify(message2))
                    elif 'operation' in result.keys() and (text.casefold() == no):
                        result["ones"] = text
                        respond2 = "Alright, please let me know if you need my assistance."
                        message2 = {"answer": respond2}
                        del result['ones']
                        del result['operation']
                        return (jsonify(message2))
                    else:
                        message2 = {"answer": "Error, please enter a valid answer"}
                        return (jsonify(message2))


                resp = random.choice(intent['responses'])
                mess = {"answer": resp}
                print("Result keys: ",result)
                return (jsonify(mess))

    rep = "Sorry, I do not understand you. Could you please rephrase that?"
    mes = {"answer": rep}
    return jsonify(mes)


if __name__ == "__main__":
    app.run(debug=True)
