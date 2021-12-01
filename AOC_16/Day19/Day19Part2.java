
import java.util.LinkedList;
public class Day19Part2 {
    private static final int NUMELVES = 3005290;
    public static void main(String[] args) {
        LinkedList<Integer> que1 = new LinkedList<>();
        LinkedList<Integer> que2 = new LinkedList<>();
        int size = NUMELVES;
        for(int i = 1; i<=size; i++) {
            if(i<=size/2)
                que1.addLast(i);
            else que2.addLast(i);
        }

        while(que1.size() + que2.size() != 1) {
            int x = que1.pollFirst();
            if(que1.size() == que2.size()) {
                que1.pollLast();
            }else {
                que2.pollFirst();
            }
            que2.addLast(x);
            int a = que2.pollFirst();
            que1.addLast(a);
        }
        System.out.println(que1.pollFirst());
    }
}
