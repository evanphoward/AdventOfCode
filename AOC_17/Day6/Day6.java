package Day6;

import java.io.File;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Created by evanphoward on 12/5/17.
 */
public class Day6 {
   public static void main(String[] args) throws Exception {
//14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4
      String check="-1";
      int steps = 0;
      LinkedList<String> combos = new LinkedList<>();
      int[] banks = {14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4};
      combos.add(toString(banks));
      while(true) {
         steps++;
         int start = findMax(banks);
         int temp = banks[start];
         banks[start]=0;
         start++;
         while(temp>0) {
            if(start==banks.length)
               start=0;
            banks[start]++;
            start++;
            temp--;
         }
         if(toString(banks).equals(check)) {
            System.out.println("Part 2: "+steps);
            System.exit(1);
         }
         if(combos.contains(toString(banks)) && check.equals("-1")) {

            check=toString(banks);
            System.out.println("Part 1: "+steps);
            steps=0;
         }
         else if(check.equals("-1"))
            combos.add(toString(banks));
      }


   }
   public static int findMax(int[] arr) {
      int temp = 0;
      for(int i=0;i<arr.length;i++)
         if(arr[temp]<arr[i])
            temp=i;
      return temp;
   }
   public static String toString(int[] arr) {
      String temp="";
      for(int i=0;i<arr.length;i++)
         temp+=arr[i]+"";
      return temp;
   }
}
