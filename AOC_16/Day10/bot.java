//Evan Howard, 18 March 2017
public class bot {
   private int high;
   private int low;
   private int lowoutput;
   private int highoutput;
   private boolean hasGiven;
   public bot(int l, int h) {
      lowoutput=l;
      highoutput=h;
      high=-1;
      low=-1;
      hasGiven=false;
   }
   public void setValue(int x) {
      if(x>low && x>high) {
         int temp=high;
         high=x;
         low=temp;
      }
      else{
         low=x;
      }
   }
   public void hasGiven(boolean b) {
      hasGiven=b;
   }
   public boolean given() {
      return hasGiven;
   }
   public int getHighOutput() {
      return highoutput;
   }
   public int getLowOutput() {
      return lowoutput;
   }
   public int getLow() {
      return low;
   }
   public int getHigh() {
      return high;
   }
}         
