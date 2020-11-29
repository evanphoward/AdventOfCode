//Evan Howard 1 March 2017
import java.util.*;
import java.io.*;
public class Driver2b
{
   private static String[][] keypad = {
        {" ", " ", "1", " ", " "}, //     1       0.     0       -------> x
        {" ", "2", "3", "4", " "}, //   2 3 4     1.   0 1 2     |
        {"5", "6", "7", "8", "9"}, // 5 6 7 8 9   2. 0 1 2 3 4   |
        {" ", "A", "B", "C", " "}, //   A B C     3.   0 1 2     |
        {" ", " ", "D", " ", " "}  //     D       4.     0       V
        };
   public static void main(String[] args) throws Exception
   {
      int x = 0;
      int y = 2;
      int count = 0;
      
      Scanner pinfile = new Scanner(new File("instructions.txt")); 
      
      while(pinfile.hasNext()) {
         pinfile.nextLine();
         count++; 
      }
      
      Scanner infile = new Scanner(new File("instructions.txt")); 
    
      String[] instruc = new String[count];
      String[] answers = new String[count];
      
      for(int i=0;i<instruc.length;i++)
         instruc[i]=infile.nextLine();
         
      infile.close();
      
      for(int k=0;k<instruc.length;k++) {
         for(int i=0;i<instruc[k].length();i++) {
            switch(instruc[k].charAt(i)) {
               case 'U': 
                  x += x < (keypad[0].length) && !keypad[y][x + 1].equals(" ") ? 1 : 0;
                  break;
               case 'L': 
                  x -= x > 0 && !keypad[y][x - 1].equals(" ") ? 1 : 0;
                  break;
               case 'R': 
                  y -= y > 0 && !keypad[y - 1][x].equals(" ") ? 1 : 0;
                  break;
               case 'D': 
                  y += y < (keypad.length - 1) && !keypad[y + 1][x].equals(" ") ? 1 : 0;
                  break;
            }
         }
         answers[k]=keypad[y][x];
      }
      
      System.out.print("The code is ");
      for(int i=0;i<answers.length;i++)
         System.out.print(answers[i]);
                           
   }
}
