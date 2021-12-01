//Evan Howard 12 March 2017
import java.security.*;
   
public class Driver5
{
   private static String s = "reyedfim";
   public static void main(String[] args) throws Exception
   {
      int counter1 = 0;
      int counter2 = 0;
      int pcounter;
      String hash;
      char[] password1 = new char[8];
      char[] password2 = new char[8];
      for(int i=0;counter2<8;i++) {
         pcounter=counter2;
         hash=md5(s+i);
         for(int k=0;k<5;k++) {
            if(hash.charAt(k)!='0')
               break;
            if(k==4) {
               if(counter1 < 8) {
                  password1[counter1] = hash.charAt(5);
                  counter1++;
               }
               if(Character.isDigit(hash.charAt(5))&&Character.getNumericValue(hash.charAt(5))<8) {
                  if(password2[Character.getNumericValue(hash.charAt(5))]==0) {
                     counter2++;
                     password2[Character.getNumericValue(hash.charAt(5))]+=hash.charAt(6);
                  }
               }
            }
         }
         if(pcounter!=counter2)
            System.out.println(counter2+"");
      }
      System.out.print("Part 1: ");
      for(int i=0;i<8;i++)
         System.out.print(password1[i]);
      System.out.println();

      System.out.print("Part 2: ");
      for(int i=0;i<8;i++)
         System.out.print(password2[i]);
      System.out.println();
   }
   private static String md5(String s) throws Exception {
      MessageDigest m=MessageDigest.getInstance("MD5");
      m.update(s.getBytes());
      byte[] digest = m.digest();
      StringBuffer sb = new StringBuffer();
      for(byte b : digest) {
         sb.append(String.format("%02x", b & 0xff));
      }
      return sb.toString();
   }
}