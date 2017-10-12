public class NumberConverter {
	String numb;
    boolean subsequent = false;
    public NumberConverter(String number) {
    	numb = number;
    }
    String [] append ={"thousand","million","billion","trillion","zillion"};
    public  int countFig(){
    	return numb.length();
    }
    public int quotient(){
       	return ( numb.length()/3);
    }
    public int modulus(){
    	return (numb.length()%3);
    }
   
    public String tens(int start, int end){
   	String tens = numb.substring(start,end);
  	String unit = numb.substring((start-1),(end-1));
  	String result;
    	if (tens.equals(String.valueOf(0))){
    		tens = "";
    		unit = unit(start-1,end-1);
    	}
    	else if (tens.equals(String.valueOf(1))){
    		if (unit.equals(String.valueOf(0))){
    			tens = "ten";
    			unit = "";
    		}
    		else if (unit.equals(String.valueOf(1))){
    			tens = "eleven";
    			unit = "";
    		}
    		else if (unit.equals(String.valueOf(2))){
    			unit = "";
    			tens = "twelve";
    		}
    		else if (unit.equals(String.valueOf(3))){
    			unit = "";
    			tens = "thirteen";
    		}
    		else if (unit.equals(String.valueOf(4))){
    			unit = "";
    			tens = "fourteen";
    		}
    		else if (unit.equals(String.valueOf(5))){
    			unit = "";
    			tens = "fifteen";
    		}
    		else if (unit.equals(String.valueOf(6))){
    			unit = "";
    			tens = "sixteen";
    		}
    		else if (unit.equals(String.valueOf(7))){
    			unit = "";
    			tens = "seventeen";
    		}
    		else if (unit.equals(String.valueOf(8))){
    			unit = "";
    			tens = "eighteen";
    		}
    		else if (unit.equals(String.valueOf(9))){
    			unit = "";
    			tens = "nineteen";
    		}
    	}
    	else if (tens.equals(String.valueOf(2))){
    		tens = "twenty";
    		unit = unit(start-1,end-1);
    	}
    	else if (tens.equals(String.valueOf(3))){
    		tens = "thirty";
    		unit = unit(start-1,end-1);
    	}
    	else if (tens.equals(String.valueOf(4))){
    		tens = "fourty";
    		unit = unit(start-1,end-1);
    	}
    	else if (tens.equals(String.valueOf(5))){
    		tens = "fifty";
    		unit = unit(start-1,end-1);
    	}
    	else if (tens.equals(String.valueOf(6))){
    		tens = "sixty";
    		unit = unit(start-1,end-1);
    	}
    	else if (tens.equals(String.valueOf(7))){
    		tens = "seventy";
    		unit = unit(start-1,end-1);
    	}
	    else if (tens.equals(String.valueOf(8))){
    		tens = "eighty";
    		unit = unit(start-1,end-1);
    	}

    	else if (tens.equals(String.valueOf(9))){
    		tens = "ninety";
    		unit = unit(start-1,end-1);
    	}
    	else {
    		System.out.println("a wrong tens has beeen inputed");
    		System.exit(0);
    	}
    	if (tens == "" && unit == ""){
    		result = " ";
    	}
    	else {
    	result = tens+" "+unit;
    	}
    return result;
    }
    public String unit(int start,int end){
    	String unit = numb.substring(start,end);
    	if ((unit.equals(String.valueOf(0)))  ){
    		unit = "";
    	}
    	else if (unit.equals(String.valueOf(1))){
    		unit = "one";
    	}
    	else if (unit.equals(String.valueOf(2))){
    		unit = "two";
    	}
    	else if (unit.equals(String.valueOf(3))){
    		unit = "three";
    	}
    	else if (unit.equals(String.valueOf(4))){
    		unit = "four";
    	}
    	else if (unit.equals(String.valueOf(5))){
    		unit = "five";
    	}
    	else if (unit.equals(String.valueOf(6))){
    		unit = "six";
    	}
    	else if (unit.equals(String.valueOf(7))){
    		unit = "seven";
    	}
    	else if (unit.equals(String.valueOf(8))){
    		unit = "eight";
    	}
    	else if (unit.equals(String.valueOf(9))){
    		unit = "nine";
    	}
	    else {
    		System.out.println("a wrong value has beeen inputed");
    		
    		System.exit(0);
    	}
    	return unit;
    }
    
    public String hund(int start , int end){
    	String hund = unit(start,end);
    	if (hund != ""){
    		if (tens(start-1,end-1) == " "){
    			hund += " hundred ";
    		}
    		else{
    			hund += " hundred and ";
    		}	
    	}
    	else{
    		if (subsequent && (tens(start-1,end-1) != " ") ){
    			hund += "and ";
   			}
   		}   	
    	String result = hund+tens(start-1,end-1);
    	return result;
    } 
    
    public String thous (int start,int end){
    	String thous = unit(start,end);
    	if (thous != "" ){
    		subsequent = true;
    		thous += " "+append[0]+" ";
    	}
    	thous = thous+hund(start-1,end-1);
       	return thous;
    }	
    
    
    public String tensThous (int start, int end){
	String allTens = tens(start,end);
    
    	if (allTens != " "){
    		subsequent = true;
    		subsequent = true;
    		allTens += " "+append[0]+" ";
    		
    	}		
    	allTens = allTens+hund(start-2, end-2);
    	return allTens;
       } 	  
    
   public String hundThous (int start, int end){
   		String hund = unit(start,end);
    	if (hund != ""){
    		subsequent = true;
    		if (tens(start-1,end-1) == " "){
    			hund += " hundred thousand";
    		}
    		else{
    			hund += " hundred and ";
    		}	
    	}
    	String result = hund+tensThous(start-1,end-1);
    	return result;
    } 	  
   
   public String mill (int start,int end){
	String mill = unit(start,end);
    	if (mill != "" ){
    		subsequent = true;
    		mill += " "+append[1]+" ";
    	}
    	mill = mill + hundThous(start-1,end-1);
       	return mill;
    }	
 
   public String tensMill (int start, int end){
  	String tensMill = tens(start,end); 
    	if (tensMill != " "){
    		subsequent = true;
    		tensMill += " "+append[1]+" ";		
    	}		
    	tensMill = tensMill+hundThous(start-2, end-2);
    	return tensMill;
       } 	      
    
   public String hundMill (int start, int end){
  	String hundMill = unit(start,end);
    	if (hundMill != ""){
    		subsequent = true;
    		if (tens(start-1,end-1) == " "){
    			hundMill += " hundred million";
    		}
    		else{
    			hundMill += " hundred and ";
    		}	
    	}
    	String result = hundMill+tensMill(start-1,end-1);
    	return result;
    } 	     
    
	public String bill (int start,int end){
	String bill = unit(start,end);
    	if (bill != "" ){
    		subsequent = true;
    		bill += " "+append[2]+" ";
    	}
    	bill = bill + hundMill(start-1,end-1);
       	return bill;
    }	
 
   public String tensBill (int start, int end){
  	String tensBill = tens(start,end); 
    	if (tensBill != " "){
    		subsequent = true;
    		tensBill += " "+append[2]+" ";		
    	}		
    	tensBill = tensBill+hundMill(start-2, end-2);
    	return tensBill;
       } 	      
    
  public String hundBill (int start, int end){
  	String hundBill = unit(start,end);
    	if (hundBill != ""){
    		subsequent = true;
    		if (tens(start-1,end-1) == " "){
    			hundBill += " hundred billion";
    		}
    		else{
    			hundBill += " hundred and ";
    		}	
    	}
    	String result = hundBill+tensBill(start-1,end-1);
    	return result;
    }    
  
  public String trill (int start,int end){
	String trill = unit(start,end);
    	if (trill != "" ){
    		subsequent = true;
    		trill += " "+append[3]+" ";
    	}
    	trill = trill + hundBill(start-1,end-1);
       	return trill;
    }	
 
  public String tensTrill (int start, int end){
  	String tensTrill = tens(start,end); 
    	if (tensTrill != " "){
    		subsequent = true;
    		tensTrill += " "+append[3]+" ";		
    	}		
    	tensTrill = tensTrill+hundBill(start-2, end-2);
    	return tensTrill;
       } 	      
    
  public String hundTrill (int start, int end){
  	String hundTrill = unit(start,end);
    	if (hundTrill != ""){
    		subsequent = true;
    		if (tens(start-1,end-1) == " "){
    			hundTrill += " hundred trillion";
    		}
    		else{
    			hundTrill += " hundred and ";
    		}	
    	}
    	String result = hundTrill+tensTrill(start-1,end-1);
    	return result;
    }    
  
  public String zill (int start,int end){
	String zill = unit(start,end);
    	if (zill != "" ){
    		subsequent = true;
    		zill += " "+append[4]+" ";
    	}
    	zill = zill + hundTrill(start-1,end-1);
       	return zill;
    }	
 
  public String tensZill (int start, int end){
  	String tensZill = tens(start,end); 
    	if (tensZill != " "){
    		subsequent = true;
    		tensZill += " "+append[4]+" ";		
    	}		
    	tensZill = tensZill+hundZill(start-2, end-2);
    	return tensZill;
       } 	      
    
  public String hundZill (int start, int end){
  	String hundZill = unit(start,end);
    	if (hundZill != ""){
    		subsequent = true;
    		if (tens(start-1,end-1) == " "){
    			hundZill += " hundred zillion";
    		}
    		else{
    			hundZill += " hundred and ";
    		}	
    	}
    	String result = hundZill+tensZill(start-1,end-1);
    	return result;
    }    
         	  
    public String check (){
    	int qout = quotient();
    	String result ="";
    	int remain = modulus();
    	if (qout == 0){
    		if (remain == 0){
    			System.out.println("Enter a figure pls!!!"); 
    		}
    		else if (remain == 1){
    			result = unit(0,1);
    		}
    		else if (remain == 2){
    			result = tens(1,2);
    		}
    	}
    	else if (qout == 1){
    		if (remain == 0){
    			result = hund(2,3);
    		}
    		else if (remain == 1){
    			result = thous(3,4);
    		}	
    		else if (remain == 2){
    			result = tensThous(4,5);
    		}
    	}
    	else if (qout == 2){
    		if (remain == 0){
    			result = hundThous(5,6);
    		}
    		else if (remain == 1){
    			result = mill(6,7);
    		}	
			else if (remain == 2){
				result = tensMill(7,8);
			}
    	}
   
    	else if (qout == 3){
    		if (remain == 0){
    			result = hundMill(8,9);
    		}
    		else if (remain == 1){
    			result = bill(9,10);
    		}	
    		else if (remain == 2){
    			result = tensBill(10,11);
    		}
    	}
    	else if (qout == 4){
    		if (remain == 0){
    			result = hundBill(11,12);
    		}
    		else if (remain == 1){
    			result = trill(12,13);
    		}	
			else if (remain == 2){
				result = tensTrill(13,14);
			}
    	}
    	else if (qout == 5){
    		 if (remain == 0){
    			result = hundTrill(14,15);
    		}
    		else if (remain == 1){
    			result = zill(15,16);
    		}	
    		else if (remain == 2){
    			result = tensZill(16,17); 
    		}
    	}
    	else if (qout == 6){
    		if (remain == 0){
    			result = hundZill(17,18);
    		}
    		else {
    			System.out.println("figure out of bound: why "+ 
    				"would you enter such a value? na only you "+ 
    					"won chop the whole!!!");
    			System.exit(0);
    		}	

    	}
    	else {
    		System.out.println("figure out of bound: why "+ 
    				"would you enter such a value? na only you "+ 
    					"waka come!!!");
    		System.exit(0);	
    	}
    	return result;
    }
  /*  public String subsequentUnit (int start,int end,int elementPosition){
    	String allUnit = unit(start,end);
    	
    	if (allUnit != ""){
    		subsequent = true;
    		controlAppend = true;
    		//allUnit += " "+append[elementPosition]+" ";
    		//if(unit(start-1,end-1) == "" && (tens(1,2) != "" || unit(0,1) != "")){
    		//	thous += "and ";
    		//}
    	}
    	else {
    		allUnit += "";
    		}
    		if(elementPosition >0 ){
    			allUnit = allUnit+subsequentHund(start-1, end-1, elementPosition-1);
    		}
    		if (elementPosition == 0 && controlAnd == 0){
    			allUnit += hund(start-1, end-1);
    		}
    	if(controlAppend){
    		allUnit += " "+append[elementPosition]+" ";
    	}	
    	return allUnit;
    }	
    public String subsequentTens (int start, int end, int elementPosition){
    	//subsequent = true;
    	String allTens = tens(start,end);
    	if (allTens != ""){
    		subsequent = true;
    		controlAppend = true;
    		allTens += " "+append[elementPosition]+" ";
    		
    	}
    	else {
    		allTens += "";	
    	}
    	if(elementPosition > 0 ){ 		
    		allTens = allTens+subsequentHund(start-2, end-2, elementPosition-1);
    	}
    	if (elementPosition == 0 && controlAnd == 0){
    			allTens += hund(start-2, end-2);
    	}
    	return allTens;
    	
    } 	  
    public String subsequentHund (int start, int end, int elementPosition){
    	String allHund = "";
    	if (unit(start,end) != ""){
    		allHund = hund(start,end);
    		subsequent = true;
    		controlAppend = true;
    			allHund += " "+append[elementPosition]+" ";		
    	
    	}
    	
    	else{
    		allHund = subsequentTens(start-1, end-1, elementPosition);
    	}
    	if(elementPosition > 0 ){
    			allHund = allHund+subsequentHund(start-3, end-3, elementPosition-1);
    		}
    	if (elementPosition == 0 && controlAnd == 0){
    			allHund = hund(start-3, end-3);
    	}		
    	return allHund;
    	
    }*/ 	  
    
}
