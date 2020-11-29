//Evan Howard 28 February 2017
import java.util.*;
import java.io.*;
public class Driver1b
{
   public static void main(String[] args) throws Exception
   {
      int count = 0;
      Scanner infile = new Scanner(new File("directions.txt"));  
    
      String direc = infile.nextLine();
      infile.close();
   
      String[] directions = direc.split(", ");
      String[] coords = new String[directions.length*200];
      for(int i = 0;i<coords.length;i++)
         coords[i]="wdag";
      
      int north,south,west,east,heading,ns,ew,total;
      north = south = west = east = heading = ns = ew = total = 0;
      
      loop:
      for(int i=0;i<directions.length;i++) {
         char turn = directions[i].charAt(0);
         int amount = Integer.parseInt(directions[i].substring(1));
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
            case 0: 
               for(int h=0;h<amount;h++) {
                  north++;
                  ns = north-south;
                  ew = east-west;
                  coords[count]=ns+","+ew;
                  count++;
                  for(int k=0;k<coords.length;k++)
                     if(coords[count-1].equals(coords[k]) && count-1!=k)
                        break loop;
               }
               break;
            case 1:                   
               for(int h=0;h<amount;h++) {
                  east++;
                  ns = north-south;
                  ew = east-west;
                  coords[count]=ns+","+ew;
                  count++;
                  for(int k=0;k<coords.length;k++)
                     if(coords[count-1].equals(coords[k]) && count-1!=k)
                        break loop;
               }
               break;
            case 2:                   
               for(int h=0;h<amount;h++) {
                  south++;
                  ns = north-south;
                  ew = east-west;
                  coords[count]=ns+","+ew;
                  count++;
                  for(int k=0;k<coords.length;k++)
                     if(coords[count-1].equals(coords[k]) && count-1!=k)
                        break loop;
               }
               break;
            case 3:                   
               for(int h=0;h<amount;h++) {
                  west++;
                  ns = north-south;
                  ew = east-west;
                  coords[count]=ns+","+ew;
                  count++;
                  for(int k=0;k<coords.length;k++)
                     if(coords[count-1].equals(coords[k]) && count-1!=k)
                        break loop;
               }
               break;
         }
      }
      
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