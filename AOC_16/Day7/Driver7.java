//Evan Howard 12 March 2017
import java.util.*;
import java.io.*;
   
public class Driver7
{
   private static final int COUNT = 2000;
   public static void main(String[] args) throws Exception
   {
      String ips;
      boolean bracket=false;
      boolean tls=false;
      int total = 0;
   
      Scanner infile = new Scanner(new File("ips.txt"));
   
      for(int i=0;i<COUNT;i++) {
         bracket=false;
         tls=false;
         ips=infile.nextLine();
         tls:
         for(int k=3;k<ips.length();k++) {
            if(ips.charAt(k)=='[')
               bracket=true;
            else if(ips.charAt(k)==']')
               bracket=false;
            if(ips.charAt(k)==ips.charAt(k-3)&&ips.charAt(k-2)==ips.charAt(k-1)&&ips.charAt(k)!=ips.charAt(k-1)) {
               if(bracket==true) {
                  tls=false;
                  break tls;
               }
               else
                  tls=true;
            }
         }
         if(tls)
            total++;
      }
      System.out.print(total+"");
   }
}
