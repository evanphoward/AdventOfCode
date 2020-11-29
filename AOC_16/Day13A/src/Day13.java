//Evan Howard, 18 March 2017
public class Day13
{
    private static char[][] map = new char[100][100];
    public static void main(String[] args) throws Exception
    {
        int sum;
        for(int y=0;y<100;y++)
            for(int x=0;x<100;x++) {
                if(x==1 && y== 1)
                    map[y][x]='S';
                else if(x==31 && y==39)
                    map[y][x]='E';
                else {
                    sum=x*x + 3*x + 2*x*y + y + y*y;
                    sum+=1358;
                    if(isEven(sum))
                        map[y][x]='_';
                    else
                        map[y][x]='#';
                }
            }

        for(int y=0;y<100;y++) {
            for(int x=0;x<100;x++)
                System.out.print(map[y][x]);
            System.out.println("");
        }
    }
    private static boolean isEven(int x) {
        int count =0;
        String s=Integer.toBinaryString(x);
        for(int i=0;i<s.length();i++)
            if(s.charAt(i)=='1')
                count++;
        return count%2==0;
    }
}