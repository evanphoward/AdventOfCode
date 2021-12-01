import java.io.File;
import java.util.Scanner;

/**
 * Created by evanphoward on 3/31/17.
 */
public class Driver15 {
    private static final int NUM = 6;
    public static void main(String[] args) throws Exception {
        Disc[] discs = new Disc[NUM];
        Scanner infile = new Scanner(new File("Discs"));
        for(int i=0;i< discs.length;i++) {
            String[] ndisc = infile.nextLine().split(" ");
            ndisc[11] = ndisc[11].substring(0, ndisc[11].length() - 1);
            discs[i]=new Disc(Integer.parseInt(ndisc[3]),Integer.parseInt(ndisc[11]));
        }

        System.out.println("Part 1: " + solveDiscs(discs));

        Disc[] discs_copy = new Disc[NUM + 1];
        for(int i = 0; i < discs.length; i++) {
            discs_copy[i] = discs[i];
        }
        discs_copy[NUM] = new Disc(11, 0);

        System.out.println("Part 2: " + solveDiscs(discs_copy));
    }

    private static int solveDiscs(Disc[] discs) {
        int time = 0;
        while(true) {
            int prevtime = time;
            timer:
            for(int i=0;i<discs.length;i++) {
                time++;
                discs[i].setPosition(time);
                if(discs[i].getPosition()!=0) {
                    time=prevtime;
                    time++;
                    break timer;
                }
                if(i==discs.length-1) {
                    return prevtime;
                }
            }
        }
    }
}
