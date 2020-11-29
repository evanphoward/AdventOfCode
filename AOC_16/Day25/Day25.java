import java.io.File;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Created by evanphoward on 4/9/17.
 */
public class Day25 {
    private static int a,b,c,d;
    private static String[] instruc;
    private static LinkedList<Character> outList;
    private static final int COUNT = 30;
    public static void main(String[] args) throws Exception
    {
        a=3;
        b=d=c=0;
        int preva;
        String[] temp;
        outList = new LinkedList<>();
        instruc = new String[COUNT];
        Scanner infile = new Scanner(new File("instructions"));

        for(int i=0;i<COUNT;i++)
            instruc[i]=infile.nextLine();


        for(a=158;true;a++) {
            preva = a;
            System.out.println(a);
            out:
            for (int i = 0; i < COUNT; i++) {
                if(outList.size()>6 && outList.getLast()!=outList.get(outList.size()-3)) {
                    outList.clear();
                    a = preva;
                    break out;
                }
                temp = instruc[i].split(" ");
                switch (temp[0]) {
                    case "cpy":
                        if (temp[1].equals("a") || temp[1].equals("b") || temp[1].equals("c") || temp[1].equals("d"))
                            set(temp[2], temp[1]);
                        else
                            set(temp[2], Integer.parseInt(temp[1]));
                        break;
                    case "jnz":
                        if (ret(temp[1]) != 0) {
                            if (temp[2].equals("a") || temp[2].equals("b") || temp[2].equals("c") || temp[2].equals("d"))
                                i += (ret(temp[2])) - 1;
                            else
                                i += Integer.parseInt(temp[2]) - 1;
                        }

                        break;
                    case "inc":
                        inc(temp[1]);
                        break;
                    case "dec":
                        dec(temp[1]);
                        break;
                    case "out":
                        out(temp[1]);
                        break;


                }
            }
        }
        }
    private static void out(String s) {
        System.out.println(ret(s));
        outList.add((char)(ret(s)));
    }
    private static void set(String s,int x) {
        switch(s) {
            case "a":
                a=x;
                break;
            case "b":
                b=x;
                break;
            case "c":
                c=x;
                break;
            case "d":
                d=x;
                break;
        }
    }
    private static void set(String s,String y) {
        switch(s) {
            case "a":
                a=ret(y);
                break;
            case "b":
                b=ret(y);
                break;
            case "c":
                c=ret(y);
                break;
            case "d":
                d=ret(y);
                break;
        }
    }
    private static void inc(String s) {
        switch(s) {
            case "a":
                a++;
                break;
            case "b":
                b++;
                break;
            case "c":
                c++;
                break;
            case "d":
                d++;
                break;
        }
    }
    private static void dec(String s) {
        switch(s) {
            case "a":
                a--;
                break;
            case "b":
                b--;
                break;
            case "c":
                c--;
                break;
            case "d":
                d--;
                break;
        }
    }
    private static int ret(String s) {
        switch(s) {
            case "a":
                return a;
            case "b":
                return b;
            case "c":
                return c;
            case "d":
                return d;
            default:
                return Integer.parseInt(s);
        }
    }
}
