import java.io.File;
import java.util.Scanner;

/**
 * Created by evanphoward on 4/7/17.
 */
public class Day23 {
    private static int a,b,c,d;
    private static String[] instruc;
    private static final int COUNT = 26;
    public static void main(String[] args) throws Exception
    {
        b=d=c=0;
        a=7;
        String[] temp = new String[3];
        instruc = new String[COUNT];
        Scanner infile = new Scanner(new File("instructions"));

        for(int i=0;i<COUNT;i++)
            instruc[i]=infile.nextLine();

        for(int i=0;i<COUNT;i++) {
            temp=instruc[i].split(" ");
            switch(temp[0]) {
                case "cpy":
                    if(temp[1].equals("a") || temp[1].equals("b") || temp[1].equals("c") || temp[1].equals("d"))
                        set(temp[2],temp[1]);
                    else
                        set(temp[2],Integer.parseInt(temp[1]));
                    break;
                case "jnz":
                    if(ret(temp[1])!=0) {
                        if(temp[2].equals("a") || temp[2].equals("b") || temp[2].equals("c") || temp[2].equals("d"))
                            i+=(ret(temp[2])) - 1;
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
                case "tgl":
                    tgl(temp[1],i);
                    break;
            }
        }
        System.out.println(a+"");
    }
    private static void tgl(String s,int i) {
        String[] temp = new String[3];
        boolean tempe = true;
        try {
            temp = instruc[ret(s)+i].split(" ");
        }
        catch(ArrayIndexOutOfBoundsException e) {
            tempe=false;
        }
        if(tempe) {
            if (temp.length > 2) {
                if(temp[0].equals("jnz"))
                    instruc[ret(s)+i] = "cpy "+temp[1]+" "+temp[2];
                else
                    instruc[ret(s)+i] = "jnz "+temp[1]+" "+temp[2];
            } else {
                if (temp[0].equals("inc"))
                    instruc[ret(s)+i] = "dec "+temp[1];
                else
                    instruc[ret(s)+i] = "inc "+temp[1];
            }
        }
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
                return 1;
        }
    }
}
