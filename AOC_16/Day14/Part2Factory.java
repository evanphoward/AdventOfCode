import java.io.File;
import java.io.PrintStream;
import java.security.MessageDigest;

/**
 * Created by evanphoward on 4/8/17.
 */
public class Part2Factory {
    private static final String s ="zpqevtbw";
    public static void main(String[] args) throws Exception {
        PrintStream outfile = new PrintStream(new File("hashes"));
        String hash;
        for(int i=0;i<30000;i++) {
            hash = md5(s + i);
            // Uncomment to generate hashes for part 2
            // This takes a really long time to generate ~25000 hashes needed
            // Maybe look into improving one day
            // for (int k = 0; k < 2016; k++)
            //     hash = md5(hash);
            outfile.println(hash);
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
