package Day10;

import java.io.File;
import java.util.InputMismatchException;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Created by evanphoward on 12/9/17.
 */
public class Day10 {
   private static LinkedList<Integer> string;
   public static void main(String[] args) throws Exception {
      //
      String input = "34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167";
      int pos = 0, skip = 0;
      string = new LinkedList<>();
      for(int i=0;i<256;i++)
         string.add(i);
      String[] temp = input.split(",");
      for(String s : temp) {
         int in = Integer.parseInt(s);
         int swaps = 0;
         for (int i = pos; swaps < in; i++) {
            swap(i % string.size(), ((pos + in - 1) - (i - pos)) % string.size());
            if (i % string.size() == ((pos + in - 1) - (i - pos)) % string.size())
               swaps++;
            else
               swaps += 2;
         }
         pos += (in + skip);
         skip++;
         pos = pos % string.size();
      }
      System.out.println("Part 1: "+(string.get(0)*string.get(1)));
      int[] instrucs = toASCII(input);
      pos = skip = 0;
      for(int i=0;i<256;i++)
         string.set(i,i);


      for(int k=0;k<64;k++) {
         for (int in : instrucs) {
            int swaps = 0;
            for (int i = pos; swaps < in; i++) {
               swap(i % string.size(), ((pos + in - 1) - (i - pos)) % string.size());
               if (i % string.size() == ((pos + in - 1) - (i - pos)) % string.size())
                  swaps++;
               else
                  swaps += 2;
            }
            pos += (in + skip);
            skip++;
            pos = pos % string.size();
         }
      }

      int[] newHash = new int[16];
      int xor=string.get(0)^string.get(1);
      for(int i=2;i<string.size();i++) {
         if(i%16==0) {
            newHash[(i/16)-1]=xor;
            xor = string.get(i)^string.get(i+1);
            i++;
         }
         else
            xor=xor^string.get(i);
      }
      newHash[15]=xor;

      String hash = "";
      for(int i=0;i<newHash.length;i++) {
         if (Integer.toHexString(newHash[i]).length() == 1)
            hash += "0";
         hash += Integer.toHexString(newHash[i]);
      }

      System.out.println("Part 2: "+hash);






   }
   public static void swap(int i1, int i2) {
      int temp = string.get(i1);
      string.set(i1,string.get(i2));
      string.set(i2,temp);
   }
   public static int[] toASCII(String s) {
      int[] temp = new int[s.length()+5];
      char[] th = s.toCharArray();
      for(int i=0;i<th.length;i++)
         temp[i]=(int)th[i];
      temp[temp.length-5]=17;
      temp[temp.length-4]=31;
      temp[temp.length-3]=73;
      temp[temp.length-2]=47;
      temp[temp.length-1]=23;
      return temp;
   }
}
