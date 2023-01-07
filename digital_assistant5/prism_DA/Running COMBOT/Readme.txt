# COMBOT
COMBOT is a virtual robot/assistant that allows anyone, regardless of experience, to use model checking techniques to verify business processes. For this purpose, COMBOT bridges the gap between the programming language of a model checking tool and the natural language of humans. The user of COMBOT can easily ask the digital assistant to analyze, obtain and verify properties of interest using natural human language. The current version of COMBOT focuses on the verification of properties derived from the legal process-related standards and regulations ISO 15504 (Automotive Software Process and Improvement = A-SPICE). All properties are determined in the backend with the engine of the model checking tool PRISM.


###   Getting started

First, we need to make sure that Python 3 is installed on our PC. Then, the packages described in requirements.txt need to be installed, for example via pip. The tool should run with all standard operating systems.

Secondly, we need to ensure that “prism” and “prism-api” are downloaded. Please follow the instructions at https://github.com/prismmodelchecker/prism-api.
For more information on the PRISM tool, visit https://www.prismmodelchecker.org.

Thirdly, download the folder "digital_assistant5" from https://github.com/Hassan-Hage/COMBOT.git., and copy and paste the downloaded “prism” and “prism-api” folders from the previous step into the folder "digital_assistant5". Afterwards, copy the file "MCK.java" from the main folder of "digital_assistant5" and paste it in the folder ->  “prism-api/src/demos”
Copy the three files “py4j0.10.9.2.jar”, “py4j0.10.9.5.jar”, and “py4j-0.10.9.5.jar” in the "digital_assitant5" folder and paste it into the folder “prism/prism/lib”. This is to ensure that the “Py4J” package is installed into Java to enable the connection between Python and PRISM model checker.
Fourthly, open your computer terminal and: cd into your “prism-api” directory in the "digital_assitant5" folder, and write "make". Then, write "make test". In this step, we will activate the engine PRISM.

Finally, open your Phyton GUI (e.g. Spyder) and run “launch.py” in the directory “digital_assistant5/prism_DA”. The console of Spyder will display "http://127.0.0.1:5000/". Copy the link and paste it in a browser. Here, we recommend google chrome.

After all steps, COMBOT can used by selecting the robot on the main body.

### License

This tool is provided under the GPL v3.0 license.

### Run an example

Some results of the paper SMC4PEP: A Conversion Tool for an Automated Verification of Product Engineering Processes can be reproduced based on the files located in “digital_assistant5/prism_DA/examples”.

To run one of the examples please apply the following steps:

Run the PRISM-API as described above.

Open a Phyton GUI (e.g. Spyder).

Run “launch.py” located in the directory “digital_assistant5/prism_DA”.

The console of Spyder will display "http://127.0.0.1:5000/". Copy the link and paste it in a browser (e.g. google chrome), and press enter.

Click on the body of COMBOT and a chat will open.

Click on the button "Choose File" (english) or "Datei auswählen" (german) to select a business process described as an MDP in the PRISM syntax of your choice. (you can use an example of the folder “digital_assistant5/prism_DA/example”)

Select the button with the arrow symbol to upload the file to COMBOT. 

Now, you can ask COMBOT to analyze and verify properties of interests. We added several possible questions in the background of COMBOT to provide some ideas how to verify properties of interests, especially derived from A-SPICE.
m A-SPICE.
