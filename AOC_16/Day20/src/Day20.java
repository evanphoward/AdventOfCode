import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.regex.PatternSyntaxException;

/**
 * @author /u/Philboyd_Studge on 12/19/2016.
 * Also I kind of helped - Evan
 */
public class Day20 {

    public static void main(String[] args) throws Exception{
        List<String[]> input = getFileLinesSplit("blacklist", "-");

        TreeMap<Long, Long> blocked = new TreeMap<>();

        for (String[] each : input) {
            blocked.put(Long.parseLong(each[0]), Long.parseLong(each[1]));
        }


        Iterator<Long> i = blocked.navigableKeySet().iterator();
        Long first = i.next();
        Long last = 0L;
        Long count = 0L;

        while (i.hasNext()) {
            Long current = i.next();
            if ((blocked.get(first) + 1) > last)
                last = blocked.get(first) + 1;
            if (current > last) {
                System.out.println("unblocked " + last + " : current " + current);
                count += current - last;
            }
            first = current;

        }

        System.out.println(count);



    }
    public static List<String[]> getFileLinesSplit(String filename, String delimiter) {
        List<String[]> list = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String input;
            while ((input = br.readLine()) != null) {
                try {
                    String[] s = input.split(delimiter);
                    list.add(s);
                } catch (PatternSyntaxException pse) {
                    System.out.println("Bad regex syntax. Delimiter \"" + delimiter + " \"");
                    return null;
                }
            }
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
        return list;

    }
}