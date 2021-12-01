//Evan Howard 28 February 2017
import java.util.*;
import java.io.*;
public class Driver3
{
   public static void main(String[] args) throws Exception
   {
      int count = 0;
      
      Scanner pinfile = new Scanner(new File("triangles.txt")); 
      
      while(pinfile.hasNext()) {
         pinfile.nextLine();
         count++; 
      }
      
      Scanner infile = new Scanner(new File("triangles.txt"));
      
      int[][] lengths = new int[count][3];
      String[] temparr = new String[3];
      
      for(int i=0;i<count;i++) {
         temparr = infile.nextLine().trim().split("\\s+");
         for(int k=0;k<3;k++)
            lengths[i][k] = Integer.parseInt(temparr[k].trim());
      }
      
      int total = 0;
      int max = 0;
      
      for(int i=0;i<count;i++) {
         if(lengths[i][0]>lengths[i][1])
            max = 0;
         else
            max = 1;
         if(lengths[i][max]<lengths[i][2])
            max = 2;
         switch(max) {
            case 0: 
               if(lengths[i][1]+lengths[i][2]>lengths[i][0])
                  total++;
               break;
            case 1: 
               if(lengths[i][0]+lengths[i][2]>lengths[i][1])
                  total++;
               break;
            case 2: 
               if(lengths[i][0]+lengths[i][1]>lengths[i][2])
                  total++;
               break;
         }
      }
                     
      System.out.println("Part 1: "+total);

      total = max = 0;
      for(int i=0;i<count;i++) {
         int col = i % 3;
         int row = i - col;
         if(lengths[row][col]>lengths[row + 1][col])
            max = 0;
         else
            max = 1;
         if(lengths[row+max][col]<lengths[row + 2][col])
            max = 2;
         switch(max) {
            case 0: 
               if(lengths[row+1][col]+lengths[row+2][col]>lengths[row][col])
                  total++;
               break;
            case 1: 
               if(lengths[row][col]+lengths[row+2][col]>lengths[row+1][col])
                  total++;
               break;
            case 2: 
               if(lengths[row][col]+lengths[row+1][col]>lengths[row+2][col])
                  total++;
               break;
         }
      }

      System.out.println("Part 2: "+total);

            
    
   }
}