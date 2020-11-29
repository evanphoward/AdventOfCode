//Evan Howard 19 March 2017
import java.io.File;
import java.security.*;
import java.util.Scanner;

public class Day14
{
    private static String s = "ngcjuoqr";
    public static void main(String[] args) throws Exception {
        int counter = 0;
        int total=0;
        char temp;
        String hash;

        Scanner infile = new Scanner(new File("hashes"));
        Scanner pinfile = new Scanner(new File("hashes"));

        while (pinfile.hasNext()) {
            total++;
        pinfile.nextLine();
    }
    pinfile.close();

    String[] hashes = new String[total];

        for(int i=0;i<hashes.length;i++)
            hashes[i]=infile.nextLine();

        infile.close();

        for(int i=0;counter<64;i++) {
            hash = hashes[i];
            for (int k = 2; k < hash.length(); k++) {
                if (hash.charAt(k) == hash.charAt(k - 1) && hash.charAt(k) == hash.charAt(k - 2)) {
                    temp = hash.charAt(k);
                    out:
                    for (int j = i + 1; j <= i + 1000; j++) {
                        hash = hashes[j];
                        for (int l = 4; l < hash.length(); l++)
                            if (hash.charAt(l) == temp && hash.charAt(l) == hash.charAt(l - 1) && hash.charAt(l) == hash.charAt(l - 2) && hash.charAt(l) == hash.charAt(l - 3) && hash.charAt(l) == hash.charAt(l - 4)) {
                                counter++;
                                System.out.println(i);
                                break out;
                            }
                    }
                    break;
                }
            }
        }
    }
}