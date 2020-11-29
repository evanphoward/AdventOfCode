import java.io.File;
import java.util.*;

/**
 * Created by evanphoward on 4/7/17.
 */
public class Day21 {
    public static void main(String[] args) throws Exception{
        int total = 0;
        int first,second;
        char temp,firstl,secondl;
        Scanner pinfile = new Scanner(new File("instructions"));
        Scanner infile = new Scanner(new File("instructions"));

        LinkedList<Character> pass = new LinkedList<>();

        for(int i=97;i<=104;i++)
            pass.addLast((char)(i));

        while(pinfile.hasNext()) {
            pinfile.nextLine();
            total++;
        }
        pinfile.close();

        for(int i=0; i<total;i++) {
            first = second = 0;
            String instruc = infile.nextLine();
            switch(instruc.charAt(0)) {
                case 's':
                    switch(instruc.charAt(5)) {
                        case 'p':
                            first = Character.getNumericValue(instruc.charAt(14));
                            second = Character.getNumericValue(instruc.charAt(30));
                            temp = pass.get(second);
                            pass.set(second,pass.get(first));
                            pass.set(first,temp);
                            break;
                        case 'l':
                            firstl = instruc.charAt(12);
                            secondl =  instruc.charAt(26);
                            second = pass.indexOf(secondl);
                            pass.set(pass.indexOf(firstl),secondl);
                            pass.set(second,firstl);
                            break;
                    }
                    break;
                case 'r':
                    switch(instruc.charAt(1)) {
                        case 'o':
                            switch(instruc.charAt(7)) {
                                case 'b':
                                    first = pass.indexOf(instruc.charAt(instruc.length()-1));
                                    if(first>3)
                                        first++;
                                    first++;
                                    for(int k=0;k<first;k++)
                                        pass.addFirst(pass.removeLast());
                                    break;
                                case 'l':
                                    for(int k=0;k<Character.getNumericValue(instruc.charAt(12));k++)
                                        pass.addLast(pass.removeFirst());
                                    break;
                                case 'r':
                                    for(int k=0;k<Character.getNumericValue(instruc.charAt(13));k++)
                                        pass.addFirst(pass.removeLast());
                                    break;
                            }
                            break;
                        case 'e':
                            int count = 0;
                            first = Character.getNumericValue(instruc.charAt(18));
                            second = Character.getNumericValue(instruc.charAt(28));
                            for(int k=first;k<=(second+first)/2;k++) {
                                temp = pass.get(k);
                                pass.set(k, pass.get(second-count));
                                pass.set(second-count,temp);
                                count++;
                            }
                            break;
                    }
                    break;
                case 'm':
                    pass.add(Character.getNumericValue(instruc.charAt(28)),pass.remove(Character.getNumericValue(instruc.charAt(14))));
                    break;

            }
            for(char c : pass)
                System.out.print(c);
            System.out.println("");
        }

    }
}
