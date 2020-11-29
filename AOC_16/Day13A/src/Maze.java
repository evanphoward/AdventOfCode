import java.util.*;
public class Maze {

    public static int[][] arr = new int[100][100];

    private static class Point {
        int x;
        int y;
        Point parent;

        public Point(int x, int y, Point parent) {
            this.x = x;
            this.y = y;
            this.parent = parent;
        }

        public Point getParent() {
            return this.parent;
        }

        public String toString() {
            return "x = " + x + " y = " + y;
        }
    }

    public static Queue<Point> q = new LinkedList<Point>();

    public static Point getPathBFS(int x, int y) {

        q.clear();

        q.add(new Point(x,y, null));

        while(!q.isEmpty()) {
            Point p = q.remove();

            if (arr[p.x][p.y] == 9) {
                return p;
            }

            if(isFree(p.x+1,p.y)) {
                arr[p.x][p.y] = -1;
                Point nextP = new Point(p.x+1,p.y, p);
                q.add(nextP);
            }

            if(isFree(p.x-1,p.y)) {
                arr[p.x][p.y] = -1;
                Point nextP = new Point(p.x-1,p.y, p);
                q.add(nextP);
            }

            if(isFree(p.x,p.y+1)) {
                arr[p.x][p.y] = -1;
                Point nextP = new Point(p.x,p.y+1, p);
                q.add(nextP);
            }

            if(isFree(p.x,p.y-1)) {
                arr[p.x][p.y] = -1;
                Point nextP = new Point(p.x,p.y-1, p);
                q.add(nextP);
            }

        }
        return null;
    }


    public static boolean isFree(int x, int y) {
        if((x >= 0 && x < arr.length) && (y >= 0 && y < arr[x].length) && (arr[x][y] == 0 || arr[x][y] == 9)) {
            return true;
        }
        return false;
    }

    public static boolean isEven(int x) {
        int count =0;
        String s=Integer.toBinaryString(x);
        for(int i=0;i<s.length();i++)
            if(s.charAt(i)=='1')
                count++;
        return count%2==0;
    }
    public static void reconstruct() {
        int sum;
        for (int y = 0; y < 100; y++)
            for (int x = 0; x < 100; x++) {
                sum = x * x + 3 * x + 2 * x * y + y + y * y;
                sum += 1358;
                if (isEven(sum))
                    arr[y][x] = 0;
                else
                    arr[y][x] = 5;
            }
    }

    public static void main(String[] args) {

        reconstruct();


        Point p;



        int sum;
        for(int r=0;r<100;r++) {
            for(int c=0;c<100;c++) {
                reconstruct();
                sum = c * c + 3 * c + 2 * c * r + r + r * r;
                sum += 1358;
                if (isEven(sum)) {
                    arr[r][c]=9;
                    p = getPathBFS(1, 1);

                    if(p != null) {
                        int count = 0;

                        while (p.getParent() != null) {
                            p = p.getParent();
                            count++;
                        }

                        if (count <= 50)
                            System.out.println(c+","+r+": "+count+" steps");

                    }

                }
            }
    }
    }

}
