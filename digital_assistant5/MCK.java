package demos;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.List;

import parser.Values;
import parser.ast.ModulesFile;
import parser.ast.PropertiesFile;
import prism.Prism;
import prism.PrismDevNullLog;
import prism.PrismException;
import prism.PrismLog;
import prism.Result;
import prism.UndefinedConstants;
import py4j.GatewayServer;
import common.StopWatch;

import parser.ast.Expression;
import prism.PrismPrintStreamLog;
import simulator.SimulatorEngine;
import java.util.ArrayList;
import java.util.Arrays;


public class MCK
{   
  	public String prop2;
	public Result result;
    public Result result1;
    public Result result2;
    public Result result3;
	public Result result11;
    public Result result22;
    public Result result33;
    public Result result21;
    public Result result23;
    public Result result31;
    public Result result32;
    public Result result51;
    public double Min_WP;
    public double Max_WP;
    public double Min_SMFS;
    public double Min_SMST;
    public long NumberTransitions;
    public long NumberStates;
    public long InitialState;
    public long timer;
    public long timers;
    public long timers1;
    public long timer1;
	public String vascal1;
    public String list1;
    public String list2;
    public double max1;

	public int h;
    public int k;
    public int index;
    public double min2;
    public double sumrew;


	public Double res1;
	public Double res2;
	public Double res3;
	public Double res11;
	public Double res21;
	public Double res31;	
    public Double res12;
	public Double res22;
	public Double res32;
	public Double res33;

    public ArrayList<String> Var1;
    public ArrayList<String> Mod1;

    private ArrayList<String> javaList;


    public int i;

	public static void main(String[] args)
	{
		//new ModelCheckFromFiles().run();
		MCK app = new MCK();
	    // app is now the gateway.entry_point
	    GatewayServer server = new GatewayServer(app);
	    server.start();
	}



    public Double one_one(String baken, String baker, String baked)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);
            // Property File
			String addr2 = "../prism_DA/"+baked+".pctl";
			System.out.println("Property filename:" + addr2);
			// Parse and load a properties model for the model
			PropertiesFile propertiesFile = prism.parsePropertiesFile(modulesFile, new File(addr2));

			// Probability: 1.1
            //Model check the 0th property from the file
			System.out.println(propertiesFile.getPropertyObject(0));
			result1 = prism.modelCheck(propertiesFile, propertiesFile.getPropertyObject(0));
            res1 = (Double) (result1.getResult());
			// System.out.println("This is the result of probability of the whole process" + res1.getResult());
            System.out.println("Working Directory = " + System.getProperty("user.dir"));

            String path=System.getProperty("user.dir") +File.separator +"..";
            System.out.println("Working Directory = " + path);


            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return res1;
	}

    public Double one_two(String baken, String baker, String baked)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);
            // Property File
			String addr2 = "../prism_DA/"+baked+".pctl";
			System.out.println("Property filename:" + addr2);
			// Parse and load a properties model for the model
			PropertiesFile propertiesFile = prism.parsePropertiesFile(modulesFile, new File(addr2));

			// Probability: 1.2
            //Model check the 2nd property from the file
			System.out.println(propertiesFile.getPropertyObject(2));
			result2 = prism.modelCheck(propertiesFile, propertiesFile.getPropertyObject(2));
            res2 = (Double) (result2.getResult());
			// System.out.println("This is the result of probability of a specific module reaching final state" + result2.getResult());

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return res2;
	}


    public Double one_three(String baken, String baker, String baked)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);
            // Property File
			String addr2 = "../prism_DA/"+baked+".pctl";
			System.out.println("Property filename:" + addr2);
			// Parse and load a properties model for the model
			PropertiesFile propertiesFile = prism.parsePropertiesFile(modulesFile, new File(addr2));

			// Probability: 1.3
            //Model check the 4th property from the file
			System.out.println(propertiesFile.getPropertyObject(4));
			result3 = prism.modelCheck(propertiesFile, propertiesFile.getPropertyObject(4));
            res3 = (Double) (result3.getResult());
			// System.out.println("This is the result of probability of a specific module reaching a specific state" + result3.getResult());

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return res3;
	}

    public Double two_one(String baken, String baker)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");

			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();

            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);

			// Load the model into the simulator
			prism.loadModelIntoSimulator();
			SimulatorEngine sim = prism.getSimulator();
			
			// Create a new path and take 3 random steps
			// (for debugging purposes, we use sim.createNewPath;
			// for greater efficiency, you could use sim.createNewOnTheFlyPath();
			sim.createNewPath();


            List<Double> listy1 = new ArrayList<>(Arrays.asList());
            List<Double> listy2 = new ArrayList<>(Arrays.asList());


			for (k = 0; k < 1000; k++) {

			sim.initialisePath(null);

			for (h = 0; h < 100000; h++) {
                sim.automaticTransition();
            }
            listy1.add((double)sim.getPathSize());
            listy2.add((double)sim.getCumulativeRewardUpToPathStep((int)sim.getPathSize(),0));
            }

            double min2 = listy1.stream().mapToDouble(Double::doubleValue).min().getAsDouble();

			System.out.println("Steps to reach final state is: "+ listy1);
            System.out.println("Total Cumulative Reward is: "+ listy2);

            // System.out.println("Minimum value is: "+ min2);

            int index = listy1.indexOf(min2);
            // System.out.println("Minimum value index is: "+ index);
			sumrew=listy2.get(index);
            System.out.println("Total Cumulative Reward of the minimum step is: "+ sumrew);

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return sumrew;
	}

    public Double two_two(String zen, String faz, String baken, String baker)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);

			// Load the model into the simulator
			prism.loadModelIntoSimulator();
			SimulatorEngine sim = prism.getSimulator();

		    // Create a new path 
			// (for debugging purposes, we use sim.createNewPath;
			// for greater efficiency, you could use sim.createNewOnTheFlyPath();
            sim.createNewPath();
            // sim.createNewOnTheFlyPath()

            String specModule1= "a";
            String specState1= "a";

            List<Double> listy1 = new ArrayList<>(Arrays.asList());
			System.out.println(listy1);

            List<String> varnamd1 = new ArrayList<>(Arrays.asList());
            for (int i = 0; i < modulesFile.getNumVars(); i++) {
            varnamd1.add(specModule1+"="+specState1);
            }
            System.out.println(varnamd1);
            System.out.println(varnamd1.size());
            // System.out.println(varnamd.get(6));

            for (int i = 0; i < varnamd1.size(); i++) {
            Expression target = prism.parsePropertiesString(varnamd1.get(i)).getProperty(0);
			sim.initialisePath(null);
			while (!target.evaluateBoolean(sim.getCurrentState())) {
				sim.automaticTransition();
			}
			// System.out.println("\nA random path reaching " + target + ":");
			sim.getPathFull().exportToLog(new PrismPrintStreamLog(System.out), true, ",", null);
            // System.out.println("Path time is: " + sim.getPath().getTotalTime());
            listy1.add(sim.getPath().getTotalTime()); // [A]
            }
	        System.out.println(listy1);

            double max2 = listy1.stream().mapToDouble(Double::doubleValue).max().getAsDouble();//16.0
            double min2 = listy1.stream().mapToDouble(Double::doubleValue).min().getAsDouble();//-6.0
			System.out.println("Maximum is: " + max2);
            System.out.println("Minimum is: " + min2);

            // Minimum Days : 2.2
            //Check Minimum Process Days from the model file using simulator 
            double Min_SMFS = min2;
            System.out.println("Minimum is: " + Min_SMFS);

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return Min_SMFS;
	}


    public Double two_three(String aw, int zen2, String baken, String baker)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);

			// Load the model into the simulator
			prism.loadModelIntoSimulator();
			SimulatorEngine sim = prism.getSimulator();

		    // Create a new path 
			// (for debugging purposes, we use sim.createNewPath;
			// for greater efficiency, you could use sim.createNewOnTheFlyPath();
            sim.createNewPath();
            // sim.createNewOnTheFlyPath()

            List<Double> listy2 = new ArrayList<>(Arrays.asList());
			System.out.println(listy2);

            String specModule2 = "a";
            String specState2= "a";


            List<String> varnamd2 = new ArrayList<>(Arrays.asList());
            for (int i = 0; i < modulesFile.getNumVars(); i++) {
            varnamd2.add(specModule2+"="+specState2);
            }
            System.out.println(varnamd2);
            System.out.println(varnamd2.size());
            // System.out.println(varnamd.get(6));

            for (int i = 0; i < varnamd2.size(); i++) {
            Expression target = prism.parsePropertiesString(varnamd2.get(i)).getProperty(0);
			sim.initialisePath(null);
			while (!target.evaluateBoolean(sim.getCurrentState())) {
				sim.automaticTransition();
			}
			// System.out.println("\nA random path reaching " + target + ":");
			sim.getPathFull().exportToLog(new PrismPrintStreamLog(System.out), true, ",", null);
            // System.out.println("Path time is: " + sim.getPath().getTotalTime());
            listy2.add(sim.getPath().getTotalTime()); // [A]
            }
	        System.out.println(listy2);

            double max3 = listy2.stream().mapToDouble(Double::doubleValue).max().getAsDouble();//16.0
            double min3 = listy2.stream().mapToDouble(Double::doubleValue).min().getAsDouble();//-6.0
			System.out.println("Maximum is: " + max3);
            System.out.println("Minimum is: " + min3);

            // Minimum Days : 2.3
            //Check Minimum Process Days from the model file using simulator 
            double Min_SMST = min3;
            System.out.println("Minimum is: " + Min_SMST);

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return Min_SMST;
	}

    public Double three_one(String baken, String baker, String baked)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);
            // Property File
			String addr2 = "../prism_DA/"+baked+".pctl";
			System.out.println("Property filename:" + addr2);
			// Parse and load a properties model for the model
			PropertiesFile propertiesFile = prism.parsePropertiesFile(modulesFile, new File(addr2));

	        // Estimation Expected Minimum Days: 3.1
            //Reward check the 1st property from the file
			System.out.println(propertiesFile.getPropertyObject(1));
			result31 = prism.modelCheck(propertiesFile, propertiesFile.getPropertyObject(1));
            res31 = (Double) (result31.getResult());
			System.out.println("This is the result of probability of the whole process" + result31.getResult());

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return res31;
	}

    public Double three_two(String baken, String baker, String baked)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);
            // Property File
			String addr2 = "../prism_DA/"+baked+".pctl";
			System.out.println("Property filename:" + addr2);
			// Parse and load a properties model for the model
			PropertiesFile propertiesFile = prism.parsePropertiesFile(modulesFile, new File(addr2));

            // Estimation Expected Minimum Days: 3.2
            //Reward check the 3rd property from the file
			System.out.println(propertiesFile.getPropertyObject(3));
			result32 = prism.modelCheck(propertiesFile, propertiesFile.getPropertyObject(3));
            res32 = (Double) (result32.getResult());
			System.out.println("This is the result of an estimation of expected minimum days a specific module reaching final state" + result32.getResult());
            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return res32;
	}


    public Double three_three(String baken, String baker, String baked)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);
            // Property File
			String addr2 = "../prism_DA/"+baked+".pctl";
			System.out.println("Property filename:" + addr2);
			// Parse and load a properties model for the model
			PropertiesFile propertiesFile = prism.parsePropertiesFile(modulesFile, new File(addr2));

            // Estimation Expected Minimum Days: 3.3
            //Reward check the 5th property from the file
			System.out.println(propertiesFile.getPropertyObject(5));
			result33 = prism.modelCheck(propertiesFile, propertiesFile.getPropertyObject(5));
            res33 = (Double) (result33.getResult());
			System.out.println("This is the result of an estimation of expected minimum days a specific module reaching a specific state" + result33.getResult());

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return res33;
	}

    public long four_one(String baken, String baker)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);

            // Check total number of transitions of the processes: 4.1
            NumberTransitions = prism.buildModel(modulesFile).getNumTransitions();
			System.out.println("This is the number of transitions: " + NumberTransitions);

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return NumberTransitions;
	}

    public long four_two(String baken, String baker)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);
           
            // Check total number of states of the processes: 4.2
            NumberStates = prism.buildModel(modulesFile).getNumStates();
			System.out.println("This is the number of states: " + NumberStates);

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return NumberStates;
	}

    public long four_three(String baken, String baker)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);
            
           // Check value of initial state of the processes: 4.3
            InitialState = prism.buildModel(modulesFile).getNumStartStates();
            System.out.println("This is the number of initial states: " + InitialState);

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return InitialState;
	}

    public long four_four(String baken, String baker)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);
            
            // Check model building/ construction time: 4.4
			timer = 0;
			timer = System.currentTimeMillis();
			prism.buildModel();
			timer = System.currentTimeMillis() - timer;
            timer1 = timer;
			System.out.println("\nTime for model construction: " + timer1 + " seconds.");

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return timer1;
	}

    public long five_one(String baken, String baker, String baked)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);
            
                        // Property File
			String addr2 = "../prism_DA/"+baked+".pctl";
			System.out.println("Property filename:" + addr2);
			// Parse and load a properties model for the model
			PropertiesFile propertiesFile = prism.parsePropertiesFile(modulesFile, new File(addr2));


            // Check model checking time: 5.1
            timers = 0;
			timers = System.currentTimeMillis();
			result51 = prism.modelCheck(propertiesFile, propertiesFile.getPropertyObject(0));
            timers = System.currentTimeMillis() - timers;
            timers1 = timers;
			System.out.println("\nTime for model checking: " + timers1 + " seconds.");

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return timers1;
	}


    public String five_two(String baken, String baker)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);
            
            // Check Modules name: 5.2
            Mod1 = new ArrayList<>(Arrays.asList());
            System.out.println("This is the names of modules: ");
            for (int i = 0; i < modulesFile.getNumModules(); i++) {
            Mod1.add(modulesFile.getModuleName(i));
			System.out.println(modulesFile.getModuleName(i));
            }
            System.out.println(Mod1);

            list1 = Mod1.toString();

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
        
        return list1;
        
	}

    public String five_three(String baken, String baker)
	{
		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");
			// Initialise PRISM engine 
			Prism prism = new Prism(mainLog);
			prism.initialise();
            // Model File
			String addr1 = "../prism_DA/"+baken+baker;
			System.out.println("Model filename:" + addr1);
			// Parse and load a PRISM model from a file
			ModulesFile modulesFile = prism.parseModelFile(new File(addr1));
			prism.loadPRISMModel(modulesFile);
            
            // Check Variables name: 5.3
            Var1 = new ArrayList<>(Arrays.asList());
            javaList = new ArrayList<>();
            System.out.println("This is the names of variables: ");
            for (int i = 0; i < modulesFile.getNumVars(); i++) {
            Var1.add(modulesFile.getVarName(i));
            javaList.add(modulesFile.getVarName(i));

			System.out.println(modulesFile.getVarName(i));
            }
            System.out.println(Var1);

            list2 = Var1.toString();

            // Close down PRISM
			prism.closeDown();

		} catch (FileNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
			return list2;
	}
}

