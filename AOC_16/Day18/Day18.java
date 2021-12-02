/**
 * Created by evanphoward on 3/31/17.
 */
public class Day18 {
    private static final String FIRST = "^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^";
    public static void main(String[] args) {
        System.out.println("Part 1: " + safeTiles(FIRST, 40));
        System.out.println("Part 2: " + safeTiles(FIRST, 400000));
    }
    private static int safeTiles(String startingRow, int length) {
        String[] grid = new String[length];
        int safe = 0;
        boolean[] previ,curr;
        String prev = startingRow;
        curr = new boolean[prev.length()];
        grid[0]=FIRST;
        for(int i=1;i<length;i++) {
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
       return safe;
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
