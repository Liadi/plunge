import java.util.*;

public class Puzzle{
	public String []arr = {"1","2","3","4","5","6","7","8"," "};
	public  Puzzle(){//empty constructor
		
	}
	public void array(){
		Collections.shuffle(Arrays.asList(arr));
	}
}