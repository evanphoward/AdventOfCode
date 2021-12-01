//Evan Howard, 18 March 2017
import java.util.*;
import java.io.*;
public class Driver10
{
   private static final int COUNT = 231;
   public static void main(String[] args) throws Exception
   {
      String botNum,lowO,highO,value;
      int jump;
      Scanner infile = new Scanner(new File("instructions.txt")); 
      
      String[] instruc = new String[COUNT];
      bot[] bots = new bot[210];
      int[] output = new int[COUNT];
      
      for(int i=0;i<COUNT;i++)
         instruc[i]=infile.nextLine();
         
      infile.close();
      
      for(String s : instruc) {
         botNum=lowO=highO="";
         jump=0;
         if(s.charAt(0)=='b') {
            for(int i=4;s.charAt(i)!=' ';i++) {
               botNum+=s.charAt(i);
               jump++;
            }
            if(s.charAt(18+jump)=='b') {
               for(int i=22+jump;s.charAt(i)!=' ';i++) {
                  lowO+=s.charAt(i);
                  jump++;
               }
               for(int i=39+jump;i<s.length();i++)
                  highO+=s.charAt(i);
            }
            else {
               lowO="-";
               for(int i=25+jump;s.charAt(i)!=' ';i++) {
                  lowO+=s.charAt(i);
                  jump++;
               }
               if(lowO.equals("-0"))
                  lowO="-98425";
               if(s.charAt(38+jump)=='b')
                  for(int i=42+jump;i<s.length();i++)
                     highO+=s.charAt(i);
               else
                  highO="-8";    
            }
            bots[Integer.parseInt(botNum)] = new bot(Integer.parseInt(lowO),Integer.parseInt(highO));
         }
      }
      
      for(String s : instruc) {
         jump=0;
         botNum=value="";
         if(s.charAt(0)=='v') {
            for(int i=6;s.charAt(i)!=' ';i++) {
               value+=s.charAt(i);
               jump++;
            }
            for(int i=19+jump;i<s.length();i++)
               botNum+=s.charAt(i);
            bots[Integer.parseInt(botNum)].setValue(Integer.parseInt(value));
         }
      }
      
      end:
      while(true) {
         for(int i = 0; i < 210; i++) {
            bot b = bots[i];
            if(output[0]!=0&&output[1]!=0&&output[2]!=0) {
               System.out.println("Part 2: " + output[0]*output[1]*output[2]);
               break end;
            }
            if(b.getLow()!=-1 && b.getHigh()!=-1&&b.given()==false) {
               if(b.getLow() == 17 && b.getHigh() == 61) {
                  System.out.println("Part 1: " + i);
               }
               b.hasGiven(true);
               if(b.getLowOutput()>=0)
                  bots[b.getLowOutput()].setValue(b.getLow());
               else if(b.getLowOutput()==-98425)
                  output[0]=b.getLow();
               else
                  output[b.getLowOutput()*-1]=b.getLow();
               if(b.getHighOutput()>=0)
                  bots[b.getHighOutput()].setValue(b.getHigh());
               else
                  output[b.getHighOutput()*-1]=b.getHigh();
            }
         }
      }
            
                           
   }
}