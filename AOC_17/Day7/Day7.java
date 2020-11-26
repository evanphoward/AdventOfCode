package Day7;

import java.io.File;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Created by evanphoward on 12/6/17.
 */
public class Day7 {
   private static final int NUM = 1292;
   private static final String BASE = "ahnofa";
   public static void main(String[] args) throws Exception {
      Scanner infile = new Scanner(new File("src/Day7/instructions"));

      LinkedList<LinkedList<String>> lines = new LinkedList<>();
      String[] names = new String[NUM];
      for(int i=0;i<NUM;i++) {
         String temp = infile.nextLine();
         names[i] = temp.substring(0,temp.indexOf(" "));
      }

      infile = new Scanner(new File("src/Day7/instructions"));

      while(infile.hasNext()) {
         String temp = infile.nextLine();
         LinkedList<String> tempArr = new LinkedList<>();
         tempArr.add(temp.substring(0,temp.indexOf(" ")));
         tempArr.add(temp.substring(temp.indexOf("(")+1,temp.indexOf(")")));
         if(temp.contains("->")) {
               String[] ttemp = temp.substring(temp.indexOf(">")+2).split(", ");
               for(String s : ttemp)
                  tempArr.add(s);
            }
         lines.add(tempArr);
      }

      Disc base = makeDisc(BASE,lines,names);

      Disc unbalanced = base.getUnbalanced();
      System.out.println(unbalanced.getName()+" "+unbalanced.soleName());





     }
     public static Disc makeDisc(String s, LinkedList<LinkedList<String>> lines, String[] arr) {
      LinkedList<Disc> temp = new LinkedList<Disc>();
      LinkedList<String> discString = lines.get(getIndex(s,arr));
      for(int i=2;i<discString.size();i++)
         temp.add(makeDisc(discString.get(i),lines,arr));
      return new Disc(discString.get(0),Integer.parseInt(discString.get(1)),temp);
     }
      public static int getIndex(String s, String[] arr) {
      for(int i=0;i<arr.length;i++)
         if(arr[i].equals(s))
            return i;
      return -1;
      }
   }
