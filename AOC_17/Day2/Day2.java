package Day2;

import java.io.File;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Created by evanphoward on 12/1/17.
 */
public class Day2 {
      public static void main(String[] args) throws Exception {
         Scanner infile = new Scanner(new File("src/Day2/instructions"));

         LinkedList<String> lines = new LinkedList<>();

         while(infile.hasNext())
            lines.add(infile.nextLine());

         int sum = 0;
         for(String s : lines) {
            String[] temp = s.split("\\s+");
            label:
            for(int i=0;i<temp.length;i++) {
               int tempi = Integer.parseInt(temp[i]);
                  for(int k = 0; k<temp.length;k++)
                     if(tempi%Integer.parseInt(temp[k])==0 && k!=i) {
                        sum += tempi / Integer.parseInt(temp[k]);
                        break label;
                     }
            }
         }

         System.out.print(sum);
      }
}
