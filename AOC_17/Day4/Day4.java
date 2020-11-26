package Day4;

import java.io.File;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Created by evanphoward on 12/4/17.
 */
public class Day4 {
   public static void main(String[] args) throws Exception {
      Scanner infile = new Scanner(new File("src/Day4/instructions"));

      LinkedList<String> lines = new LinkedList<>();

      while(infile.hasNext())
         lines.add(infile.nextLine());

      boolean tempb = true;
      int sum = 0;

      for(String s : lines) {
         String[] temp = s.split("\\s+");
         for(int i=0;i<temp.length;i++) {
            String check = temp[i];
            for (int k=0;k<temp.length;k++)
               if(isAnagram(temp[k],check) && k!=i)
                  tempb = false;
         }
            if(tempb)
               sum++;
            tempb=true;
      }

      System.out.println(sum);

   }
   public static boolean isAnagram(String s1, String s2) {
      if ( s1.length() != s2.length() ) {
         return false;
      }
      s1=s1.toLowerCase();
      s2=s2.toLowerCase();
      char[] c1 = s1.toCharArray();
      char[] c2 = s2.toCharArray();
      Arrays.sort(c1);
      Arrays.sort(c2);
      String sc1 = new String(c1);
      String sc2 = new String(c2);
      return sc1.equals(sc2);
   }
}
