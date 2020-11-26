package Day13;

import java.io.File;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Created by evanphoward on 12/13/17.
 */
public class Day13 {
   public static void main(String[] args) throws Exception {
      Scanner infile = new Scanner(new File("src/Day13/instructions"));
      LinkedList<String> instrucs = new LinkedList<>();
      while(infile.hasNext())
         instrucs.add(infile.nextLine());
      Camera[] scanners = new Camera[Integer.parseInt(instrucs.getLast().substring(0,instrucs.getLast().indexOf(":")))+1];
      int count = 0;
      for(int i=0;i<scanners.length;i++) {
         String temp = instrucs.get(count);
         if(Integer.parseInt(temp.substring(0,temp.indexOf(":")))==i) {
            scanners[i] = new Camera(Integer.parseInt(temp.substring(temp.indexOf(" ") + 1)));
            count++;
         }
      }

      System.out.println("Part 1: "+(severity(scanners)-1));

      int seconds=0;
      while(severity(scanners)!=0) {
         for (Camera c : scanners)
            if(c!=null)
               c.move();
         seconds++;
      }

      System.out.println("Part 2: "+seconds);

   }

   public static int severity(Camera[] ca) {
      Camera[] scanners = new Camera[ca.length];
      for(int i=0;i<ca.length;i++)
         if(ca[i]!=null)
            scanners[i]= new Camera(ca[i]);
      int severity=0;
      for(int i=0;i<scanners.length;i++) {
         if (scanners[i] != null)
            if (scanners[i].getCurrent() == 1)
               if(i!=0)
                  severity+=(i*scanners[i].getRange());
               else
                  severity++;
         for(Camera c : scanners)
            if(c!=null)
               c.move();
      }
      return severity;
   }
}
