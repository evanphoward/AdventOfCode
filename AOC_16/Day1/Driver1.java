//Evan Howard 27 February 2017
import java.util.*;
import java.io.*;
public class Driver1
{
   public static void main(String[] args) throws Exception
   {
      int count = 0;
      Scanner infile = new Scanner(new File("Day1/directions.txt"));
    
      String direc = infile.nextLine();
      infile.close();
   
      String[] directions = direc.split(", ");
      
      int north,south,west,east,heading;
      north = south = west = east = heading = 0;
      
      for(int i=0;i<directions.length;i++) {
         char turn = directions[i].charAt(0);
         if(turn == 'L')
            if(heading != 0)
               heading--;
            else
               heading = 3;
         else if(turn == 'R')
            if(heading != 3)
               heading++;
            else
               heading = 0;
               
         switch(heading) {
            case 0: north+=Integer.parseInt(directions[i].substring(1));
               break;
            case 1: east+=Integer.parseInt(directions[i].substring(1));
               break;
            case 2: south+=Integer.parseInt(directions[i].substring(1));
               break;
            case 3: west+=Integer.parseInt(directions[i].substring(1));
               break;
         }
      }
      
      int ns = north-south;
      int ew = east-west;
      int total = 0;
      
      if(ns > 0) {
         System.out.println("You traveled "+ ns + " blocks north.");
         total+=ns;
      }
      else
      {
         System.out.println("You traveled "+ ns*-1 + " blocks south.");
         total+=ns*-1;
      }
         
      if(ew > 0){
         total+=ew;
         System.out.println("You traveled "+ ew + " blocks east.");
      }
      else{
         total+=ew*-1;
         System.out.println("You traveled "+ ew*-1 + " blocks west.");
      }
      
      System.out.println("You traveled a total of " + total + " blocks.");
         
      
   }
}
