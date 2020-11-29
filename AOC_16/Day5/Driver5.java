//Evan Howard 12 March 2017
import java.util.*;
import java.io.*;
import java.security.*;
import java.math.*;
import java.nio.charset.StandardCharsets;
   
public class Driver5
{
   private static String s = "ffykfhsq";
   public static void main(String[] args) throws Exception
   {
      int counter=0;
      int pcounter;
      String hash;
      char[] password = new char[8];
      for(int i=0;counter<8;i++) {
         pcounter=counter;
         hash=md5(s+i);
         for(int k=0;k<5;k++) {
            if(hash.charAt(k)!='0')
               break;
            if(k==4) {
               if(Character.isDigit(hash.charAt(5))&&Character.getNumericValue(hash.charAt(5))<8) {
                  if(password[Character.getNumericValue(hash.charAt(5))]==0) {
                     counter++;
                     password[Character.getNumericValue(hash.charAt(5))]+=hash.charAt(6);
                  }
               }
            }
         }
         if(pcounter!=counter)
            System.out.println(counter+"");
      }
      for(int i=0;i<8;i++)
         System.out.println(password[i]);
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