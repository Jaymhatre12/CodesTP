

// There are 100 doors in a row, all doors are initially closed. A person walks through all doors multiple times and toggle (if open then close, if close then open) them in the following way: 

// In the first walk, the person toggles every door 

// In the second walk, the person toggles every second door, i.e., 2nd, 4th, 6th, 8th, … 

// In the third walk, the person toggles every third door, i.e. 3rd, 6th, 9th, … 

// Likewise,

// In the 100th walk, the person toggles the 100th door. 


// ========================================================================================================
import java.util.*;

public class Main {
    public static void main(String[] args) {
      System.out.println("Hello, World!");
      
      String [] doors = new String[100];
      
      
      for(int i=0;i<100;i++){
        doors[i] = "Closed";
      }
      
      
    for(int j=0;j<100;j++){                                                   
      j++;                                                    
      for(int i=j;i<100;i++){
        if(doors[i]=="Closed"){
          if(i%j==0){
            doors[i]="Open";
          }
            
        } 
        else{
          if(i%j==0){
            doors[i]="Closed";
          }
        }
        i=i+j;
      }
    }
      
      int count = 0;
      for(int i=0;i<100;i++){
        if(doors[i]=="Open"){
          count+=1;
        }
      }
              System.out.println(count);

      
  }

}

