# COMBOT
COMBOT is a virtual robot / assistant to enable using model checking techniques for anyone, regardless of experience, for verifying business processes. Fur this purpose, COMBOT bridges the gap between programming language a model checking tool and the natural language of humans. The user of COMBOT can easily ask the digital assistant by using natural language of humans to analyse, obtain and verify properties of interests. The current version of COMBOT is focused on verifying properties coming from legal process-related standards and regulations ISO 15504 (Automotive Software Process and Improvement = A-SPICE). All properties are obtained using in the backend the engine of the model checking tool PRISM.

###   Getting started

First, we need to make sure that Python 3 is installed on our PC. Then, the packages described in requirements.txt need to be installed, for example via pip. The tool should run with all standard operating systems.

Secondly, we need to ensure that PRISM and PRSIM-API are downloaded (via https://www.prismmodelchecker.org).

Thirdly, download the folder "digital_assistant5" from https://github.com/Hassan-Hage/COMBOT.git., and copy and paste the downloaded folders PRISM and PRISM-API into the folder "digital_assistant5". Afterwards, copy the file "MCK.java" from the main folder of "digital_assistant5" and paste it in the folder of PRISM-API.

Fourthly, open your computer terminal and: cd into your "PRISM-API" directory in the "digital_assitant5" folder, and write "make", and write "make test". In this step, we will activate the engine PRISM.

Finally, open your Phyton GUI (e.g. Spyder) and run “launch.py” in the directory “digital_assistant5/prism_DA”. In the console of Spyder will appear "http://127.0.0.1:5000/". Copy the link and paste it in a browser. Here, we recommend google chrome.

After all steps, COMBOT can used by selecting the robot on the main body.

### License

This tool is provided under the GPL v3.0 license.

### Run an example

Some results of the paper SMC4PEP: A Conversion Tool for an Automated Verification of Product Engineering Processes can be reproduced based on the files located in “digital_assistant5/prism_DA/examples”.

To run one of the examples please apply the following steps:

Run the PRISM-API as described above.

Open a Phyton GUI (e.g. Spyder).

Run “launch.py” located in the directory “digital_assistant5/prism_DA”.

In the console of spyder will appear "http://127.0.0.1:5000/". Copy the link and paste it in a browser (e.g. google chrome), and press enter.

Click on the body of COMBOT and a chat will open.

Click on the button "Datei auswählen" to select a business process described as an MDP in the PRISM syntax of your choice. (you can use an example of the folder “digital_assistant5/prism_DA/example”)

Select the button with the arrow symbol to upload the file to COMBOT. 

Now, you can ask COMBOT to analyze and verify properties of interests. We added several possible questions in the background of COMBOT to provide some ideas how to verify properties of interests, especially coming from A-SPICE.

You need support? Contact: hassan.hage@hsu-hh.de
