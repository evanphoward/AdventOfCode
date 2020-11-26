package Day14;

import java.util.LinkedList;

/**
 * Created by evanphoward on 12/14/17.
 */
public class Day14 {
   private static LinkedList<Integer> string;
   private static int current;
   public static void main(String[] args) throws Exception {
      //
      String input = "uugsqrei";
      int used = 0;
      current = 1;
      int[][] grid = new int[128][128];

      for(int i=0;i<128;i++) {
         String bin = "";
         String temp = knotHash(input+"-"+i);
         for(int j=0;j<temp.length();j++)
            if(j+1==temp.length())
               bin+=hexToBinary(temp.substring(j));
            else
               bin+=hexToBinary(temp.substring(j,j+1));
         for(int j=0;j<128;j++) {
            if (bin.charAt(j) == '1') {
               grid[i][j] = 1;
               used++;
            }
            else
               grid[i][j] = 0;
         }
      }

      System.out.println("Part 1: "+used);

      for(int i=0;i<grid.length;i++)
         for(int j=0;j<grid.length;j++) {
            if(grid[i][j]==current) {
               current++;
               setGroup(i, j, grid);
               for(int i1=0;i1<grid.length;i1++)
                  for(int j1=0;j1<grid.length;j1++)
                     if(grid[i1][j1]==current-1)
                        grid[i1][j1]=current;
               for(int i1=0;i1<grid.length;i1++)
                  for(int j1=0;j1<grid.length;j1++)
                     if(grid[i1][j1]==-1)
                        grid[i1][j1]=current-1;
            }
         }

      System.out.println("Part 2: "+(current-1));
   }

   public static void setGroup(int i, int j, int[][] grid) {
      if(i<0 || j<0 || i>=128 || j>=128)
         return;
      if(grid[i][j]==0 || grid[i][j]==-1)
         return;
      grid[i][j]=-1;
      setGroup(i-1,j,grid);
      setGroup(i+1,j,grid);
      setGroup(i,j-1,grid);
      setGroup(i,j+1,grid);
   }

   public static String knotHash(String s) {
      int pos = 0, skip = 0;
      string = new LinkedList<>();
      for(int i=0;i<256;i++)
         string.add(i);
      int[] instrucs = toASCII(s);


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

      return hash;
   }

   public static String hexToBinary(String hex) {
         int i = Integer.parseInt(hex, 16);
         String bin = Integer.toBinaryString(i);
         int diff = 4-bin.length();
         for(int j=0;j<diff;j++)
            bin = "0"+bin;
         return bin;
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
