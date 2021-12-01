//Evan Howard 28 February 2017
import java.util.*;
import java.io.*;
public class Driver4
{
   private static final int COUNT = 1091;
   public static void main(String[] args) throws Exception
   {
      int check,id,max;
      int cool=0;
      int sum = 0;
      int counter=0;
      int pcounter=0;
      int[] temparr = new int[26];
      char[] rmax = new char[5];
      String checksum,codes,encrypt,unencrypt,ttemp;
      String[] temp;
      int[] letters = new int[26];
      ttemp = unencrypt = "";

      Scanner infile = new Scanner(new File("rooms.txt"));
   
      for(int i=0;i<COUNT;i++) {
         unencrypt = "";
         counter=0;
         for(int k=0;k<26;k++) {
            letters[k]=0;
         }
         ttemp = "";
         check=0;
         codes = infile.nextLine();
         for (int k = 0; !(Character.isDigit(codes.charAt(k))); k++)
            check++;
            
         checksum = codes.substring(check);
         encrypt = codes.substring(0,check-1);
         
         id = Integer.parseInt(checksum.substring(0,3));
         checksum = checksum.substring(4,9);
         
         
         temp = encrypt.split("-");
         for(int k=0;k<temp.length;k++)
            ttemp = ttemp+temp[k];
         codes=ttemp;
         
         for(int k=0;k<codes.length();k++)
            letters[letterToInt(codes.charAt(k))]++;
            
         max=0;
         for(int k=0;k<26;k++)
            if(letters[k]>max)
               max=letters[k];
         for(int k=0;counter<5;k++) {
            cool=0;
            pcounter=counter;
            for(int j=0;j<counter;j++) {
               temparr[j]=0;
            }
            for(int j=0;j<26;j++)
               if(letters[j]==max-k) {
                  temparr[cool]=j;
                  cool++;
                  counter++;
               }
            char[] ttemparr = new char[cool];
            for(int j=0;j<cool;j++) 
               ttemparr[j]=intToLetter(temparr[j]);
            Arrays.sort(ttemparr);
            cool=0;
            for(int j=0;j<ttemparr.length && j<5 && pcounter+cool<5;j++) {
               rmax[pcounter+cool]=ttemparr[j];
               cool++;
            }
         }
         
         for(int k=0;k<5;k++) {
            if(checksum.charAt(k)!=rmax[k])
               break;
            if(k==4) {
               sum += id;
               for(int j=0;j<encrypt.length();j++) {
                  if(encrypt.charAt(j)=='-')
                     unencrypt=unencrypt+' ';
                  else {
                     int x=letterToInt(encrypt.charAt(j));
                     x+=id;
                     x=x%26;
                     unencrypt=unencrypt+intToLetter(x);
                  }
               }
               if(unencrypt.equals("northpole object storage"))
                  System.out.println("Part 2: " + id + "");
            }
         }
               
      }
      System.out.println("Part 1: " + sum + "");
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