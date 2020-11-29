//Evan Howard 13 March 2017
import java.util.*;
import java.io.*;
   
public class Driver7b
{
   private static final int COUNT = 2000;
   public static void main(String[] args) throws Exception
   {
      String ips;
      char out,in;
      boolean bracket,aba;
      bracket=aba=false;
      int total = 0;
   
      Scanner infile = new Scanner(new File("ips.txt"));
   
      for(int i=0;i<COUNT;i++) {
         out = in = '5';
         bracket=false;
         aba=false;
         ips=infile.nextLine();
         aba:
         for(int k=2;k<ips.length();k++) {
            if(ips.charAt(k)=='[')
               bracket=true;
            else if(ips.charAt(k)==']')
               bracket=false;
            if(ips.charAt(k)==ips.charAt(k-2)&&ips.charAt(k)!=ips.charAt(k-1)&&!(bracket)) {
               out=ips.charAt(k);
               in=ips.charAt(k-1);
               for(int j=2;j<ips.length();j++) {
                  if(ips.charAt(j)=='[')
                     bracket=true;
                  else if(ips.charAt(j)==']')
                     bracket=false;
                  if(ips.charAt(j)==ips.charAt(j-2)&&ips.charAt(j)==in&&ips.charAt(j-1)==out&&bracket) {
                     aba=true;
                     break aba;
                  }
               }
               
            }
         }
         if(aba)
            total++;
      }
      System.out.print(total+"");
   }
}
