public class working_solution {
   private static String[][] keypad_part2 = {
        {" ", " ", "1", " ", " "}, //     1       0.     0       -------> x
        {" ", "2", "3", "4", " "}, //   2 3 4     1.   0 1 2     |
        {"5", "6", "7", "8", "9"}, // 5 6 7 8 9   2. 0 1 2 3 4   |
        {" ", "A", "B", "C", " "}, //   A B C     3.   0 1 2     |
        {" ", " ", "D", " ", " "}  //     D       4.     0       V
   };
   private static String[][] keypad = {
        {"1", "2", "3"}, //0. {0, 1, 2}
        {"4", "5" ,"6"}, //1. {0, 1, 2}
        {"7", "8", "9"}  //2. {0, 1, 2}
   };
   private static int x = 1, y = 1;
   private static String bathroomCode = "";

   public static void main(String[] args) {
      for (String lineCommand : inputs) {
         String[] movement = lineCommand.split("(?<=\\G.)");
      
         for (String action : movement) {
            switch (action) {
               case "R":
                  x += x < (keypad[0].length - 1) && !keypad[y][x + 1].equals(" ") ? 1 : 0;
                  break;
               case "L":
                  x -= x > 0 && !keypad[y][x - 1].equals(" ") ? 1 : 0;
                  break;
               case "U":
                  y -= y > 0 && !keypad[y - 1][x].equals(" ") ? 1 : 0;
                  break;
               case "D":
                  y += y < (keypad.length - 1) && !keypad[y + 1][x].equals(" ") ? 1 : 0;
                  break;
            }
         }
         bathroomCode += keypad[y][x];
      }
      System.out.println(bathroomCode);
   }


   private static String[] inputs = {
        "ULL",
        "RRDDD",
        "LURDL",
        "UUUUD"
   };
}