//Evan Howard, 18 March 2017
import java.util.*;
import java.io.*;
public class Driver12
{
   private static int a,b,c,d;
   private static final int COUNT = 23;
   public static void main(String[] args) throws Exception
   {
      a=b=d=c=0;
      /* uncomment this for part 2
      c=1;
      */
      String[] temp = new String[3];
      String[] instruc = new String[COUNT];
      Scanner infile = new Scanner(new File("instructions.txt")); 
      
      for(int i=0;i<COUNT;i++)
         instruc[i]=infile.nextLine();    
         
      for(int i=0;i<COUNT;i++) {
         temp=instruc[i].split(" ");
         switch(temp[0]) {
            case "cpy":
               if(temp[1].equals("a") || temp[1].equals("b") || temp[1].equals("c") || temp[1].equals("d"))
                  set(temp[2],temp[1]);
               else
                  set(temp[2],Integer.parseInt(temp[1]));
               break;
            case "jnz":
               if(ret(temp[1])!=0)
                  i+=Integer.parseInt(temp[2])-1;
               break;
            case "inc":
               inc(temp[1]);
               break;
            case "dec":
               dec(temp[1]);
               break;
         }
      }
      System.out.println(a+"");                 
   }
   private static void set(String s,int x) {
      switch(s) {
         case "a":
            a=x;
            break;
         case "b":
            b=x;
            break;
         case "c":
            c=x;
            break;
         case "d":
            d=x;
            break;
      }
   }
   private static void set(String s,String y) {
      switch(s) {
         case "a":
            a=ret(y);
            break;
         case "b":
            b=ret(y);
            break;
         case "c":
            c=ret(y);
            break;
         case "d":
            d=ret(y);
            break;
      }
   }
   private static void inc(String s) {
      switch(s) {
         case "a":
            a++;
            break;
         case "b":
            b++;
            break;
         case "c":
            c++;
            break;
         case "d":
            d++;
            break;
      }
   }
   private static void dec(String s) {
      switch(s) {
         case "a":
            a--;
            break;
         case "b":
            b--;
            break;
         case "c":
            c--;
            break;
         case "d":
            d--;
            break;
      }
   }
   private static int ret(String s) {
      switch(s) {
         case "a":
            return a;
         case "b":
            return b;
         case "c":
            return c;
         case "d":
            return d;
         default:
            return 1;
      }
   }

}