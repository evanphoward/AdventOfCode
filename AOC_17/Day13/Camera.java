package Day13;

/**
 * Created by evanphoward on 12/13/17.
 */
public class Camera {
   private int range,current;
   private boolean movingDown;

   public Camera(int range) {
      this.range = range;
      this.current = 1;
      movingDown=true;
   }
   public Camera(Camera c) {
      this.range = c.getRange();
      this.current = c.getCurrent();
      this.movingDown = c.isMovingDown();
   }

   public int getRange() {
      return range;
   }

   public int getCurrent() {
      return current;
   }

   public boolean isMovingDown() {
      return movingDown;
   }

   public void move() {
      if(current==range && movingDown)
         movingDown=false;
      else if(current==1 && !movingDown)
         movingDown=true;

      if(movingDown)
         current++;
      else
         current--;
   }
}
