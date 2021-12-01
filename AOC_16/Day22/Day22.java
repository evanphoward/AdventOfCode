import java.io.File;
import java.util.*;

/**
 * Created by evanphoward on 4/9/17.
 */
public class Day22 {
    public static void main(String[] args) throws Exception {
        Scanner infile = new Scanner(new File("nodes"));
        int count=0;
        List<String[]> temp = new ArrayList<>();
        while(infile.hasNext())
            temp.add(infile.nextLine().split("\\s+"));

        infile.close();

        int[] used = new int[temp.size()];
        int[] avail = new int[temp.size()];

        for(int i=0;i<used.length;i++) {
            String[] temps = temp.get(i);
            used[i] = Integer.parseInt(temps[2].substring(0,temps[2].length()-1));
            avail[i] = Integer.parseInt(temps[3].substring(0,temps[3].length()-1));
        }

        for(int a = 0;a<used.length;a++)
            for(int b = 0;b<used.length;b++)
            if(used[a]!=0 && a!=b)
                if (used[a] <= avail[b])
                    count++;

        System.out.println("Part 1: " + count);
    }
}