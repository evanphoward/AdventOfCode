//Evan Howard 28 February 2017
import java.util.*;
import java.io.*;
public class Driver2
{
   public static void main(String[] args) throws Exception
   {
      int num = 5;
      int count = 0;
      
      Scanner pinfile = new Scanner(new File("instructions.txt")); 
      
      while(pinfile.hasNext()) {
         pinfile.nextLine();
         count++; 
      }
      
      Scanner infile = new Scanner(new File("instructions.txt")); 
    
      String[] instruc = new String[count];
      int[] answers = new int[count];
      
      for(int i=0;i<instruc.length;i++)
         instruc[i]=infile.nextLine();
         
      infile.close();
      
      for(int k=0;k<instruc.length;k++) {
         for(int i=0;i<instruc[k].length();i++)
            switch(instruc[k].charAt(i)) {
               case 'U': 
                  if(num != 1 && num != 2 && num != 3)
                     num-=3;
                  break;
               case 'L': 
                  if(num != 1 && num != 4 && num != 7)
                     num--;
                  break;
               case 'R': 
                  if(num != 3 && num != 6 && num != 9)
                     num++;
                  break;
               case 'D': 
                  if(num != 7 && num != 8 && num != 9)
                     num+=3;
                  break;
            }
         answers[k]=num;
      }
      
      System.out.print("The code is ");
      for(int i=0;i<answers.length;i++)
         System.out.print(answers[i]);
                           
   }
}