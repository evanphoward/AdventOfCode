package Day8;

import java.io.File;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Created by evanphoward on 12/7/17.
 */
public class Day8 {
   private static LinkedList<Register> registers;
   public static void main(String[] args) throws Exception {
      Scanner infile = new Scanner(new File("src/Day8/instructions"));
      registers = new LinkedList<Register>();

      while (infile.hasNext()) {
         boolean b = true;
         String temp = infile.nextLine();
         temp = temp.substring(0, temp.indexOf(" "));
         for (Register r : registers)
            if (r.getName().equals(temp))
               b = false;
         if (b)
            registers.add(new Register(temp, 0));
      }

      infile = new Scanner(new File("src/Day8/instructions"));
      boolean isTrue;

      int max = findMax();

      while (infile.hasNext()) {
         String[] temp = infile.nextLine().split(" ");
         switch(temp[5]) {
            case ">":
               isTrue = registers.get(indexOf(temp[4])).getValue() > Integer.parseInt(temp[6]);
               break;
            case "<":
               isTrue = registers.get(indexOf(temp[4])).getValue() < Integer.parseInt(temp[6]);
               break;
            case "<=":
               isTrue = registers.get(indexOf(temp[4])).getValue() <= Integer.parseInt(temp[6]);
               break;
            case ">=":
               isTrue = registers.get(indexOf(temp[4])).getValue() >= Integer.parseInt(temp[6]);
               break;
            case "==":
               isTrue = registers.get(indexOf(temp[4])).getValue() == Integer.parseInt(temp[6]);
               break;
            case "!=":
               isTrue = registers.get(indexOf(temp[4])).getValue() != Integer.parseInt(temp[6]);
               break;
            default:
               isTrue=false;
         }
         if(isTrue)
            if(temp[1].equals("dec"))
               registers.get(indexOf(temp[0])).addValue(Integer.parseInt(temp[2])*-1);
            else if(temp[1].equals("inc"))
               registers.get(indexOf(temp[0])).addValue(Integer.parseInt(temp[2]));
         if(findMax()>max)
            max=findMax();
      }

      System.out.println("Part 1: "+findMax());
      System.out.println("Part 2: "+max);
   }
      public static int indexOf(String s) {
         for(int i=0;i<registers.size();i++)
            if(registers.get(i).getName().equals(s))
               return i;
         System.out.println(s);
         return -1;
   }

      public static int findMax() {
         int max = 0;
         for(int i=0;i<registers.size();i++)
            if(registers.get(i).getValue()>registers.get(max).getValue())
               max=i;
         return registers.get(max).getValue();
      }
}
