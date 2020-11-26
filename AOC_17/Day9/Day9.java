package Day9;

import java.io.File;
import java.util.Scanner;

/**
 * Created by evanphoward on 12/9/17.
 */
public class Day9 {
   public static void main(String[] args) throws Exception {
      Scanner infile = new Scanner(new File("src/Day9/instructions"));
      String group = infile.nextLine();
      //String group = "{{<a!>},{<a!>},{<a!>},{<ab>}}";
      char[] stream = group.toCharArray();
      boolean inGarbage = false;
      int points = 0,level = 0, chars = 0;
      for(int i=0;i<stream.length;i++) {
         if(stream[i]=='!')
            i++;
         else
            if(!inGarbage)
               switch (stream[i]) {
                  case '{':
                     level++;
                     break;
                  case '}':
                     points += level;
                     level--;
                     break;
                  case '<':
                     inGarbage = true;
               }
            else if(stream[i]=='>')
               inGarbage=false;
            else
               chars++;
      }
      System.out.println(points+" points");
      System.out.println(chars+" garbage characters");
   }
}
