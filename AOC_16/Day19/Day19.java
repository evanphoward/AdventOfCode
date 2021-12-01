/**
 * Created by evanphoward on 4/5/17.
 */
public class Day19 {
    private static final int NUMELVES = 3005290;
    public static void main(String[] args) {
        boolean found;
        int skip,presents,last;
        Elf[] elves = new Elf[NUMELVES];
        for(int i=0;i<elves.length;i++)
            elves[i] = new Elf();


        out:
        while(true) {
            for(int i=0;i<elves.length;i++) {
                last = 0;
                presents = 0;
                if (elves[i].getPresents() != 0) {
                    found = true;
                    skip = 0;
                    while (found) {
                        if (elves[(i + 1 + skip)%NUMELVES].getPresents() != 0) {
                            elves[i].setPresents(elves[i].getPresents() + elves[(i + 1 + skip)%NUMELVES].getPresents());
                            elves[(i + 1 + skip)%NUMELVES].setPresents(0);
                            found = false;
                        } else
                            skip++;
                    }
                    for (int k = 0; k < elves.length; k++) {
                        if (elves[k].getPresents() != 0) {
                            last = k;
                            presents++;
                        }
                        if (presents == 2)
                            break;
                        if (k == elves.length - 1)
                            break out;
                    }
                }
            }
        }
        last++;
        System.out.println(last+"");
    }
}
