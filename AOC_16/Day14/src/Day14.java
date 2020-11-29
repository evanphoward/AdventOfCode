//Evan Howard 19 March 2017
import java.security.*;
//import java.math.*;
//import java.nio.charset.StandardCharsets;

    public class Day14
    {
        private static String s = "ngcjuoqr";
        public static void main(String[] args) throws Exception
        {
            int counter=0;
            String hash;

            for(int i=0;counter<64;i++) {
                hash=md5(s+i);
                for(int k=2;k<hash.length();k++) {
                    if(hash.charAt(k)==hash.charAt(k-1) && hash.charAt(k)==hash.charAt(k-2) && hash.charAt(k)!=hash.charAt(k-3) && hash.charAt(k)!=hash.charAt(k+1)) {
                    }
                }

            }
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
