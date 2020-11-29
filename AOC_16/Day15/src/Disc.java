/**
 * Created by evanphoward on 3/31/17.
 */
public class Disc {
    private int myHoles;
    private int myPosition;
    private int origPos;
    public Disc(int h, int p) {
        myHoles = h;
        origPos = p;
    }
    public int getPosition() {
        return myPosition;
    }
    public void setPosition(int t) {
        myPosition = (t+origPos)%myHoles;
    }
}
