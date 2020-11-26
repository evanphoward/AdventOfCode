package Day5;

import java.io.File;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Created by evanphoward on 12/5/17.
 */
public class Day5 {
   public static void main(String[] args) throws Exception {
      Scanner infile = new Scanner(new File("src/Day5/instructions"));

      LinkedList<Integer> instrucs = new LinkedList<>();

      while(infile.hasNext())
         instrucs.add(Integer.parseInt(infile.nextLine()));

      int curr = 0,steps = 0;

      while(curr>=0&&curr<instrucs.size()) {
         steps++;
         int temp = curr;
         curr += instrucs.get(curr);
         if(instrucs.get(temp)>=3)
            instrucs.set(temp,instrucs.get(temp)-1);
         else
            instrucs.set(temp,instrucs.get(temp)+1);
      }

      System.out.println(steps);


   }
}
