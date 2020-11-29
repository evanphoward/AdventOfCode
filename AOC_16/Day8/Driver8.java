//Evan Howard 14 March 2017 - Happy Pi Day!
import java.util.*;
import java.io.*;
public class Driver8
{
   private static int[][] panel;
   private static final int COUNT = 153;
   public static void main(String[] args) throws Exception
   {
      Scanner infile = new Scanner(new File("instructions.txt")); 
      String col,times;
      int total =0;
      
      String[] instruc = new String[COUNT];
      panel = new int[50][6];
      
      for(int r=0;r<6;r++)
         for(int c=0;c<50;c++)
            panel[c][r]=0;
      
      for(int i=0;i<COUNT;i++)
         instruc[i]=infile.nextLine();
         
      infile.close();
      
      for(int i=0;i<instruc.length;i++) {
         col=times="";
         if(Character.isDigit(instruc[i].charAt(5))) {
            if(instruc[i].length()>8) {
               col=col+instruc[i].charAt(5)+instruc[i].charAt(6);
               rect(Integer.parseInt(col),Character.getNumericValue(instruc[i].charAt(8)));
            }
            else
               rect(Character.getNumericValue(instruc[i].charAt(5)),Character.getNumericValue(instruc[i].charAt(7)));
         }
         else {
            if(instruc[i].charAt(7)=='c') {
               if(Character.isDigit(instruc[i].charAt(17))) {
                  col=col+instruc[i].charAt(16)+instruc[i].charAt(17);
                  times=times+instruc[i].charAt(22);
               }
               else {
                  col=col+instruc[i].charAt(16);
                  times=times+instruc[i].charAt(21);
               }
               vertrotate(Integer.parseInt(col),Integer.parseInt(times));
            }
            if(instruc[i].charAt(7)=='r') {
               if(instruc[i].length()>19) {
                  col=col+instruc[i].charAt(13);
                  times=times+instruc[i].charAt(18)+instruc[i].charAt(19);
               }
               else {
                  col=col+instruc[i].charAt(13);
                  times=times+instruc[i].charAt(18);
               }
               horizrotate(Integer.parseInt(col),Integer.parseInt(times));
            }
         
         }
      }
      
      for(int r=0;r<6;r++){
         for(int c=0;c<50;c++) {
            if(panel[c][r]==1)
               System.out.print("#");
            else
               System.out.print(" ");
         }
         System.out.println("");
      }
            
                           
   }
   private static void horizrotate(int row,int x)
   {
      for(int k=0;k<x;k++) {
         int wrap = panel[49][row];
         for(int i=49;i>0;i--)
            panel[i][row]=panel[i-1][row];
         panel[0][row]=wrap;
      }
   }
   private static void vertrotate(int col,int x)
   {
      for(int k=0;k<x;k++) {
         int wrap = panel[col][5];
      
         for(int i=5;i>0;i--)
            panel[col][i]=panel[col][i-1];
         panel[col][0]=wrap;
      }
   }
   private static void rect(int x, int y)
   {
      for(int j=0;j<x;j++)
         for(int k=0;k<y;k++)
            panel[j][k]=1;
   }
}