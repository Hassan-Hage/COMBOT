import py4j.GatewayServer;

public class Py4j {
	
public int addition(int first, int second, int third, int forth) {
	    return first + second + third + forth;
	  }

public int states(int ab) {
	ab=6;
	System.out.println("States"); 
    return ab;
  }

public int probability(int ab) {
	ab=87;
	System.out.println("Probability"); 
    return ab;
  }

public int transitions(int ab) {
	ab=12;
	System.out.println("Transitions"); 
    return ab;
  }

public String prisms(String a) {
	a="PRISM probability and states";
    return a;
  }

	    /**
	     * @param args the command line arguments
	     */
	    public static void main(String[] args) {
	        // TODO code application logic here
	     Py4j app = new Py4j();
	    // app is now the gateway.entry_point
	    GatewayServer server = new GatewayServer(app);
	    server.start();
	    }
}
