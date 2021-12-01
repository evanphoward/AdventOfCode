//Evan Howard 12 March 2017
import java.util.*;
import java.io.*;
   
public class Driver6
{
   private static final int COUNT = 598;
   private static final int LETTERS = 8;
   public static void main(String[] args) throws Exception
   {
      String encrypt;
      String[] message = new String[COUNT];
      int[] letters = new int[26];
      int min,minlet;
      int max,maxlet;
      String mess1 = "";
      String mess2 = "";
   
      Scanner infile = new Scanner(new File("message.txt"));
   
      for(int i=0;i<COUNT;i++)
         message[i]=infile.nextLine();
      
      for(int i=0;i<LETTERS;i++) {
         encrypt="";
         for(int k=0;k<26;k++)
            letters[k]=0;
            
         for(int k=0;k<COUNT;k++)
            encrypt=encrypt+message[k].charAt(i);
            
         for(int k=0;k<encrypt.length();k++)
            letters[letterToInt(encrypt.charAt(k))]++;
      
            
         min=minlet=100;
         max = maxlet = 0;
         for(int k=0;k<26;k++) {
            if(letters[k] > max) {
               max = letters[k];
               maxlet = k;
            }
            if(letters[k]<min) {
               min=letters[k];
               minlet=k;
            }
         }
            
         mess1 = mess1 + intToLetter(maxlet);
         mess2=mess2+intToLetter(minlet);
      }

      System.out.println("Part 1: " + mess1);
      System.out.println("Part 2: " + mess2);
         
      
   
   }
   private static int letterToInt(char x) {
      switch(x) {
         case 'a': 
            return 0;
               
         case 'b': 
            return 1;
                  
         case 'c': 
            return 2;
                  
         case 'd': 
            return 3;
                  
         case 'e': 
            return 4;
                  
         case 'f': 
            return 5;
                  
         case 'g': 
            return 6;
                  
         case 'h': 
            return 7;
                  
         case 'i': 
            return 8;
                  
         case 'j': 
            return 9;
                  
         case 'k': 
            return 10;
                  
         case 'l': 
            return 11;
                  
         case 'm': 
            return 12;
                  
         case 'n': 
            return 13;
                  
         case 'o': 
            return 14;
                  
         case 'p': 
            return 15;
                  
         case 'q': 
            return 16;
                  
         case 'r': 
            return 17;
                  
         case 's': 
            return 18;
                  
         case 't': 
            return 19;
                  
         case 'u': 
            return 20;
                  
         case 'v': 
            return 21;
                  
         case 'w': 
            return 22;
                  
         case 'x': 
            return 23;
                  
         case 'y': 
            return 24;
                  
         case 'z': 
            return 25;
                  
      }
      return 27;
   }
   private static char intToLetter(int x) {
      switch(x) {
         case 0: 
            return 'a';
                     
         case 1: 
            return 'b';
                     
         case 2: 
            return 'c';
                     
         case 3: 
            return 'd';
                     
         case 4: 
            return 'e';
                     
         case 5: 
            return 'f';
                     
         case 6: 
            return 'g';
                     
         case 7: 
            return 'h';
                     
         case 8: 
            return 'i';
                     
         case 9: 
            return 'j';
                     
         case 10: 
            return 'k';
                     
         case 11: 
            return 'l';
                     
         case 12: 
            return 'm';
                     
         case 13: 
            return 'n';
                     
         case 14: 
            return 'o';
                     
         case 15: 
            return 'p';
                     
         case 16: 
            return 'q';
                     
         case 17: 
            return 'r';
                     
         case 18: 
            return 's';
                     
         case 19: 
            return 't';
                     
         case 20: 
            return 'u';
                     
         case 21: 
            return 'v';
                     
         case 22: 
            return 'w';
                     
         case 23: 
            return 'x';
                     
         case 24: 
            return 'y';
                     
         case 25: 
            return 'z';
                     
      }
      return '!';
   }

}
