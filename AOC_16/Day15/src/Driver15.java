import java.io.File;
import java.util.Scanner;

/**
 * Created by evanphoward on 3/31/17.
 */
public class Driver15 {
    private static final int NUM = 7;
    public static void main(String[] args) throws Exception {
        Disc[] discs = new Disc[NUM];
        int time = 0;
        Scanner infile = new Scanner(new File("Discs"));
        for(int i=0;i< discs.length;i++) {
            String[] ndisc = infile.nextLine().split(" ");
            discs[i]=new Disc(Integer.parseInt(ndisc[0]),Integer.parseInt(ndisc[1]));
        }

        correct:
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
                    System.out.println(prevtime + "");
                    break correct;
                }
            }
        }

    }
}
