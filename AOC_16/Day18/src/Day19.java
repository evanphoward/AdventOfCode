/**
 * Created by evanphoward on 3/31/17.
 */
public class Day19 {
    private static final String FIRST = ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^";
    private static final int LENGTH = 400000;
    public static void main(String[] args) {
        String[] grid = new String[LENGTH];
        int safe = 0;
        boolean[] previ,curr;
        String prev = FIRST;
        curr = new boolean[prev.length()];
        grid[0]=FIRST;
        for(int i=1;i<LENGTH;i++) {
            prev="."+prev+".";
            previ = convertToBool(prev);
            for(int k=1;k<prev.length()-1;k++) {
                    if(isTrap(previ[k-1],previ[k],previ[k+1]))
                    curr[k-1]=true;
                    else
                        curr[k-1]=false;

            }
            prev = convertToString(curr);
            grid[i]=prev;
        }

        for(String s : grid) {
            for(int i=0;i<s.length();i++)
                if(s.charAt(i)=='.')
                    safe++;
        }
       System.out.print(safe+"");


    }
    private static boolean isTrap(boolean l, boolean c, boolean r) {
        if(l && c && !r)
            return true;
        if(c && r && !l)
            return true;
        if(l && !c && !r)
            return true;
        if(!l && !c && r)
            return true;
        return false;
    }
    private static boolean[] convertToBool(String s) {
        boolean[] b = new boolean[s.length()];
        for(int i=0;i<s.length();i++)
            b[i] = s.charAt(i)=='^';
        return b;
    }
    private static String convertToString(boolean[] b) {
        String s = "";
        for(int i=0;i<b.length;i++) {
            if(b[i])
                s+="^";
            else
                s+=".";
        }
        return s;
    }
}
