package Day11;

import java.io.File;
import java.util.Scanner;


public class Day11 {

   enum HexDir {
      n(0, -1), ne(1, -1), se(1, 0), s(0, 1), sw(-1, 1), nw(-1, 0);

      int dx, dy;

      HexDir(int dx, int dy) { this.dx = dx; this.dy = dy; }

   }


   private static int hexDistance(int x, int y) {
      return ((Math.abs(x) + Math.abs(y) + Math.abs(x + y))/ 2);
   }


   public static void main(String[] args) throws Exception {
      Scanner infile = new Scanner(new File("src/Day11/instructions"));
      String input = infile.nextLine();
      int x = 0;
      int y = 0;

      int furthest = 0;
      int dist = 0;

      for (String each : input.split(",")) {
         HexDir current = HexDir.valueOf(each);
         x += current.dx;
         y += current.dy;
         dist = hexDistance(x, y);
         if (dist > furthest) furthest = dist;

      }
      System.out.println("Part 1: "+dist);
      System.out.println("Part 2: "+furthest);
   }
}
