import json
import ast


dell = """
{
    "intents": [
         {
        "tag": "greeting",
        "patterns": [
          "Hi","What's up?"
          "Hey",
          "How are you",
          "Is anyone there?",
          "Hello",
          "Good day",
          "How's it going?"
        ],
        "responses": [
          "Hello, my name is Combot, thanks for using my service. How can i help you?",
          "Hello, how can i help you?",
          "Hi there, i'm Combot, what can I do for you?",
          "Hi there, how can I help?"
        ]
      },
       {
        "tag": "goodbye",
        "patterns": ["Bye", "bye-bye","See you later","Goodbye","Ciao","so long"],
        "responses": [
          "See you soon, thanks for using my service",
          "Have a nice day",
          "Bye! Feel free to use my service again."
        ]
      },
    
      {
        "tag": "level",
        "patterns": [
          "What is the highest reachable A-SPICE level?",
          "A-SPICE level?","topmost A-SPICE level?",
          "highest reachable A-SPICE level?","maximum reachable A-SPICE level?",
          "highest A-SPICE level?","maximum A-SPICE level?",
          "What is the highest A-SPICE level that we can currently achieve?"
          "highest A-SPICE level?",
        ],
        "responses": [
          "As of right now, Level 2 is the highest reachable A-SPICE Level. Should I list down all the Generic Practice of A-SPICE level 2? (Yes / No)",
        ]
      },

      {
        "tag": "one_one",
        "patterns": [
          "Please verify if GP 2.1.7 is met","Could you please verify GP 2.1.7?",
          "Please verify if GP 2.1.3 is met","Could you please verify GP 2.1.3?",
          "Verify GP 2.1.7","Verify GP 2.1.3","Check GP 2.1.7","any delay?",
          "Check GP 2.1.3","2.1.7","2.1.3","Is there any delay?",
          "Probability of the whole process?","Odds of the whole process?",
          "What is the probability of the whole process?",
          "What is the chance of reaching final state of the whole process?","What are the odds of reaching final state of the whole process?",
          "What is the possibility of reaching final state of the whole process?",
          "What is the probability of the whole process reaching final state?"
          
        ],
        "responses": [

        ]
      },

      {
        "tag": "one_two",
        "patterns": [
          "Please verify the probability of a specific module reaching final state","check probability",
          "Probability of a specific module reaching final state","odds specific module final state?",
          "Probability specific module reaching final state","probability specific module final state?",
          "What is the probability of a specific module reaching final state?",
          "specific module reaching final state?","specific module final state?",

        ],
        "responses": [
          "Please enter variable number: ",
        ]
      },

      {
        "tag": "one_three",
        "patterns": [
          "Please verify the probability of a specific module reaching a specific state",
          "Probability of a specific module reaching specific state",
          "Probability specific module reaching specific state","chance specific module specific state?",
          " What is the probability of a specific module reaching a specific state?",
          "specific module specific state?","probability specific module specific state?",

        ],
        "responses": [
          "Please enter variable number2: ",
        ]
      },
      
      {
        "tag": "two_one",
        "patterns": [
          "Minimum days for performing whole process?","least days whole process?",
          "Tell me, how long is the duration of the whole process?",
          "Duration of the whole process?","least duration of reaching whole process?","smallest duration of reaching end state of whole process?",
          "Days of the whole process?", "Minimum days of reaching end state of the whole process?",
          "Minimum days of the whole process?","least days of reaching end state of whole process?","smallest days of reaching end state of whole process?",
          "what is the minimum days for performing whole process?",
        ],
        "responses": [

        ]
      },

    

      {
        "tag": "three_one",
        "patterns": [
          "Estimation of expected minimum days for performing whole process",
          "what is the expected minimum days of my whole process?","what is the predicted minimum days of my whole process?",
          "Tell me, expected minimum days of my whole process?","what is the anticipated days of my whole process?",
          "Expected minimum days of my whole process?","what is the anticipated least days of my whole process?",
          "How long is the expected minimum days of whole process?",
          "What is the estimation of expected minimum days for performing whole process",
        ],
        "responses": [

        ]
      },
      
      {
        "tag": "three_two",
        "patterns": [
          "Estimation of expected minimum days of a specific module reaching final state",
          "Estimation expected minimum days of a specific module reaching final state",
          "Estimation minimum days specific module reaching final state",
          "What is the estimation of expected minimum days of a specific module reaching final state?",

        ],
        "responses": [
          "Please enter variable number3: ",
        ]
      },

      {
        "tag": "three_three",
        "patterns": [
          "Estimation of expected minimum days of a specific module reaching a specific state",
          "Estimation expected minimum days a specific module reaching specific state",
          "Expected minimum days specific module reaching specific state","Estimation expected minimum days specific module specific state",
        ],
        "responses": [
          "Please enter variable number4: ",
        ]
      },
      {
        "tag": "four_one",
        "patterns": [
          "Total number of transitions of the processes?","overall number of transitions of the processes?",
          "Tell me, what is the total number of transitions in my processes?","full number transitions of the processes?",
          "Number of transitions of my process?","total amount of transitions of the processes?","sum number of transitions?",
          "Total number of transitions in my process?","how many transitions do I have in my processes?","sum transitions?",
          "What is the number of transitions in my process?","total transitions?"
        ],
        "responses": [

        ]
      },

      
      {
        "tag": "four_two",
        "patterns": [
          "Total number of states of the processes?","overall number of states of the processes?",
          "Tell me, what is the total number of states in my processes?","full number states of the processes?",
          "Number of states of my process?","total amount of states of the processes?","sum number of states?",
          "Number of states in my process?","how many states do I have in my processes?","sum states?",
          "What is the number of states in my process?","total states?"
        ],
        "responses": [

        ]
      },

     {
        "tag": "four_three",
        "patterns": [
          "Value of initial state of process?","Value of first state of process?",
          "Number of initial state of process?","how many first state i have in my process?",
          "Tell me, what is the value of initial state in my processes?","how many initial state i have in my process?",
          "what is the value of initial state of my process?",
          "Initial state value of my process?",
          "Initial state number of my process?",
          "What is the number of initial state in my process?","initial state?"
        ],
        "responses": [

        ]
      },

     {
        "tag": "four_four",
        "patterns": [
          "What is building model time",
          "building and construction model time",
          "What is the building model time of the process?",
          "Tell me, what is the building model time?",
          "what is the model construction time of my process?","construction model time?",
          "Tell me the construction time of the model?","building model time?",
          "what is construction building model time of my process?","building time?",
          "What is the number of building model time in my process?","construction time?"
        ],
        "responses": [

        ]
      },

  {
        "tag": "five_one",
        "patterns": [
          "What is checking model time",
          "checking model time",
          "What is the checking model time of the process?",
          "Tell me, what is the checking model time?",
          "what is the model checking time of my process?",
          "Tell me the checking time of the model?",
          "what is model checking time of my process?",
          "What is the number of checking model time in my process?"
        ],
        "responses": [

        ]
      },

      
      {
        "tag": "five_two",
        "patterns": [
          "What is modules name","every modules name",
          "list down all modules name",
          "What is all the modules name of my model?",
          "Tell me, what is all modules names?",
          "what is the modules name of my process?",
          "What is the name of all modules my MDP model?","all modules",
          "Name all modules my MDP model"
        ],
        "responses": [

        ]
      },

     {
        "tag": "five_three",
        "patterns": [
          "What is variables name","every variables name",
          "list down all variables name",
          "What is all the variables name of my model?",
          "Tell me, what is all variables names?",
          "what is the variables name of my process?",
          "What is the name of all variables my MDP model?","all variables",
          "Name all variables my MDP model"
        ],
        "responses": [

        ]
      },

    ]
  }
"""


bell = ast.literal_eval(dell)
#val1 = json.loads(json.dumps(val))

#print(bell)
#print(val1)
#print(value)

#print(wer)


for intent in bell['intents']:
     tag = intent['tag']
     rezpon = intent['responses']

#     #if tag == "greeting":
#         #print("greeting responses: ",intent['responses'])



#     if tag == "probability":
#         rezpon.append("The probability of reaching final state is: " + str(sums1) + "%")
#         print("probability responses: ",intent['responses'])

#     if tag == "transitions":
#         rezpon.append("The total number of transitions is: 44")
#         print("transitions responses: ",intent['responses'])

            
    # rezpon = intent['responses']
    # rezpon.append(sum_state)
    # rezpon.append(sum_prob)
    # rezpon.append(sum_transit)
  


print(bell)
