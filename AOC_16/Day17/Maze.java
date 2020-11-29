import gnu.trove.list.TCharList;
import gnu.trove.list.array.TCharArrayList;
import gnu.trove.map.TIntObjectMap;
import gnu.trove.map.hash.TIntObjectHashMap;

import java.util.IntSummaryStatistics;
import java.util.stream.IntStream;

import com.google.common.base.Charsets;
import com.google.common.hash.HashCode;
import com.google.common.hash.HashFunction;
import com.google.common.hash.Hashing;

public class Maze {

    public static final TIntObjectMap<char[]> success = new TIntObjectHashMap<>();
    public static final HashFunction md5 = Hashing.md5();
    public static final String INPUT = "pgflpeqp";
    public static final char[] dirs = { 'U', 'D', 'L', 'R' };
    public static final int[] dx = { 0, 0, -1, 1 };
    public static final int[] dy = { -1, 1, 0, 0 };

    public static int doors(HashCode hash) {
        final String str = hash.toString();
        int doors = 0;

        for (int i = 0; i < Maze.dirs.length; i++) {
            final char c = str.charAt(i);

            if (c >= 'b' && c <= 'f') {
                doors |= 1 << i;
            }
        }

        return doors;
    }

    public static void delve(TCharList stack, int x, int y) {
        if (x == 3 && y == 3) {
            // WOW, it wanted the PATH, not just the length
//            Maze.success.add(stack.size());
            Maze.success.put(stack.size(), stack.toArray());
            return;
        }

        final int doors = Maze.doors(Maze.md5.hashString(new StringBuilder(Maze.INPUT).append(stack.toArray()), Charsets.US_ASCII));

        for (int i = 0, nx, ny; i < Maze.dirs.length; i++) {
            // Check that the door is open and we won't exit the grid by moving that way
            if ((1 << i & doors) != 0 && (Math.floorDiv(nx = x +  Maze.dx[i], 4) | Math.floorDiv(ny = y + Maze.dy[i], 4)) == 0) {
                stack.add(Maze.dirs[i]);
                Maze.delve(stack, nx, ny);
                stack.removeAt(stack.size() - 1);
            }
        }
    }

    public static void main(String[] args) {
        Maze.delve(new TCharArrayList(), 0, 0);

        final IntSummaryStatistics stats;

        System.out.println(stats = IntStream.of(Maze.success.keys()).summaryStatistics());
        System.out.println("Min path: " + String.valueOf(Maze.success.get(stats.getMax())).length());
    }
}