package Day1;

import java.io.File;
import java.util.Scanner;

/**
 * Created by evanphoward on 11/30/17.
 */
public class Day1A {
      public static void main(String[] args) throws Exception {
         Scanner infile = new Scanner(new File("src/Day1/instructions"));
         String input = infile.nextLine();
         int sum=0;

         for(int i=0;i<input.length()-1;i++) {
            int currentNum = input.charAt(i) - '0';
            //int nextNum = input.charAt(i+1) - '0'; /* Part A */
            int nextNum = input.charAt((i+(input.length()/2))%input.length()) - '0'; /* Part B */
            if(currentNum==nextNum)
               sum+=currentNum;
         }
         System.out.print(sum);
      }
}
