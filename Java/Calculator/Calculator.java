/**
 * @(#)Calculator.java
 *
 *
 * @author LIADI OMOTOLA RILWAN
 * @version 1.00 2014/8/28
 */
public class Calculator{
	public double operand (String op){
		double result = Double.valueOf(op);
		return result;
	}
	public char operator (char ch){
		char result ;
		switch(ch){
			case '_':
				result = '_';
				break;
			case '$':
				result = '$';
				break;
			case  '^':
				result = '^';
				break;
			case '+':
				result = '+';
				break;
			
			case '-':
				result = '-';
				break;
			
			case '*':
				result = '*';
				break;
			
			case '%':
				result = '%';
				break;
			
			case '/':
				result = '/';
				break;
			default:
				result = ' ';			
		}
		return result;
	}
	public double binary(double op1,char ch,double op2){
		double result;

		switch(ch){
			
			case '+':
				result = op1 + op2;
				break;
			
			case '-':
				result = op1 - op2;
				break;
			
			case '*':
				result = op1 * op2;
				break;
			case '/':
				result = op1 / op2;
				break;
			default:
			 	result = 0;
			
		}
		return result;
	}
	public double unary (char ch, double op){
		double result = 0.0;
		switch(ch){
			case '_':
				result = (-op);
				break;
			case '$':
				if (op < 0){
					break;
				}
				else{
					result = Math.sqrt(op);
				}
				break;
			case  '^':
				result = 1/(op);
				break;

			case '%':
				result = (op*0.01);
				break;

			default:
				result = 0;
		}
		return result;
	}
}