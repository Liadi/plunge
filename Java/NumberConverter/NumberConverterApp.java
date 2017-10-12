/**
 * @(#)NumberConverterApp.java
 *
 *
 * @author 
 * @version 1.00 2014/8/28
 */
import java.util.*;
import javax.swing.JOptionPane;
public class NumberConverterApp {
	public static void main (String[] args) {
		
    	Scanner input = new Scanner(System.in);
    	while ( true ){
    		String figure = JOptionPane.showInputDialog("Enter the figure to convert");
      		String stop = "stop";
      		//sentinel controlled stop
      		if (figure.equals(stop)){ 
      			System.exit(0);
      		}
      		StringBuilder buffer = new StringBuilder(figure);
      		buffer.reverse();
      		figure = buffer.toString(); 
       		NumberConverter myNumberConverter = new NumberConverter(figure);
       		JOptionPane.showMessageDialog(null, "\nfigure in words:\n"+myNumberConverter.check()+"\n","Number in Words",JOptionPane.PLAIN_MESSAGE);
      		
    	}   
    }   		 
}