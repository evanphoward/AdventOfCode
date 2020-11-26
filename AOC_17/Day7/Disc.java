package Day7;

import java.util.LinkedList;

/**
 * Created by evanphoward on 12/7/17.
 */
public class Disc {
   private LinkedList<Disc> discs;
   private int weight;
   private String name;

   public Disc(String name, int weight, LinkedList<Disc> discs) {
      this.name=name;
      this.discs = discs;
      this.weight=weight;
   }
   public int getWeight() {
      int sum = weight;
      for(Disc d : discs)
         sum+=d.getWeight();
      return sum;
   }

   public String getName() {
      return name;
   }

   public int soleName() {
      return weight;
   }

   public Disc getUnbalanced() {
      for(Disc d: discs)
         System.out.print(d.getWeight()+" ");
      System.out.println();
      int commonWeight = discs.getFirst().getWeight();
      for(Disc d1 : discs)
         if(d1.getWeight()!=commonWeight)
            for(Disc d : discs)
               if(d!=discs.getFirst())
                  if(d.getWeight()!=commonWeight && (d.getWeight()!=discs.getLast().getWeight() || d.getWeight()!=discs.get(1).getWeight()))
                     return d.getUnbalanced();
                  else if(commonWeight!=discs.getLast().getWeight() && commonWeight!=discs.get(1).getWeight())
                     return discs.getFirst().getUnbalanced();
      return this;
   }
}
