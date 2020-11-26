package Day8;

/**
 * Created by evanphoward on 12/9/17.
 */
public class Register {
   private String name;
   private int value;

   public Register(String name, int value) {
      this.name = name;
      this.value = value;
   }

   public String getName() {
      return name;
   }

   public int getValue() {
      return value;
   }

   public void addValue(int value) {
      this.value += value;
   }

}
