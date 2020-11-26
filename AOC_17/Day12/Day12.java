package Day12;

import java.io.File;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Created by evanphoward on 12/11/17.
 */
public class Day12 {
   public static void main(String[] args) throws Exception {
      Scanner infile = new Scanner(new File("src/Day12/instructions"));
      LinkedList<String> instruc = new LinkedList<>();
      LinkedList<LinkedList<Integer>> pipes = new LinkedList<>();
      LinkedList<Integer> tempL = null;
      while (infile.hasNext())
         instruc.add(infile.nextLine());
      for(int j=0;j<50;j++)
         for (String s : instruc) {
            int times = 0;
            for (LinkedList<Integer> l : pipes)
               if (l.contains(Integer.parseInt(s.substring(0, s.indexOf(" "))))) {
                  tempL = l;
                  times++;
               }
            if (tempL == null) {
               pipes.add(new LinkedList<>());
               tempL = pipes.getLast();
               tempL.add(Integer.parseInt(s.substring(0,s.indexOf(" "))));
            }
            if (tempL.contains(Integer.parseInt(s.substring(0, s.indexOf(" "))))) {
               String[] temp = s.substring(s.indexOf(">") + 2).split(", ");
               for (String t : temp)
                  if (!tempL.contains(Integer.parseInt(t)))
                     tempL.add(Integer.parseInt(t));
            }
            if(times>1) {
               LinkedList<Integer> one = new LinkedList<>();
               LinkedList<Integer> two = new LinkedList<>();
               for(LinkedList<Integer> l : pipes)
                  if(l.contains(Integer.parseInt(s.substring(0, s.indexOf(" ")))))
                     if(one.isEmpty())
                        one=l;
                     else {
                        two = l;
                        break;
                     }
               for(int i : two)
                  if(!one.contains(i))
                     one.add(i);
               pipes.remove(two);
            }
            tempL=null;
         }
      for(LinkedList<Integer> l : pipes)
         if(l.contains(0))
            System.out.println("Part 1: "+l.size());
      System.out.println("Part 2: "+pipes.size());
   }
}
