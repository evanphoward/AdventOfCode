import sun.awt.image.ImageWatched;

import java.io.File;
import java.util.*;

/**
 * Created by evanphoward on 4/7/17.
 */
public class Part2 {
    private static final String SCRAMBLED = "fbgdceah";
    public static void main(String[] args) throws Exception{
        int total = 0;
        int first,second;
        char temp,firstl,secondl;
        Scanner pinfile = new Scanner(new File("instructions"));
        Scanner infile = new Scanner(new File("instructions"));

        LinkedList<Character> pass = new LinkedList<>();

        for(int i=0;i<SCRAMBLED.length();i++)
            pass.add(SCRAMBLED.charAt(i));


        while(pinfile.hasNext()) {
            pinfile.nextLine();
            total++;
        }
        pinfile.close();

        String[] instruc = new String[total];

        for(int i=0;i<instruc.length; i++)
            instruc[i]=infile.nextLine();


        for(int i=instruc.length-1; i>=0;i--) {
            first = second = 0;
            switch(instruc[i].charAt(0)) {
                case 's':
                    switch(instruc[i].charAt(5)) {
                        case 'p':
                            first = Character.getNumericValue(instruc[i].charAt(14));
                            second = Character.getNumericValue(instruc[i].charAt(30));
                            temp = pass.get(second);
                            pass.set(second,pass.get(first));
                            pass.set(first,temp);
                            break;
                        case 'l':
                            firstl = instruc[i].charAt(12);
                            secondl =  instruc[i].charAt(26);
                            second = pass.indexOf(secondl);
                            pass.set(pass.indexOf(firstl),secondl);
                            pass.set(second,firstl);
                            break;
                    }
                    break;
                case 'r':
                    switch(instruc[i].charAt(1)) {
                        case 'o':
                            switch(instruc[i].charAt(7)) {
                                case 'b':
                                    LinkedList<Character> templ = new LinkedList<>(pass);
                                    while(true) {
                                        if (pass.equals(rotateBased(templ, templ.indexOf(instruc[i].charAt(instruc[i].length() - 1)))))
                                            break;
                                        templ.addLast(templ.removeFirst());
                                    }
                                    for(int w=0;w<pass.size();w++)
                                        pass.set(w,templ.get(w));
                                        break;
                                case 'l':
                                    for(int k=0;k<Character.getNumericValue(instruc[i].charAt(12));k++)
                                        pass.addFirst(pass.removeLast());
                                    break;
                                case 'r':
                                    for(int k=0;k<Character.getNumericValue(instruc[i].charAt(13));k++)
                                        pass.addLast(pass.removeFirst());
                                    break;
                            }
                            break;
                        case 'e':
                            int count = 0;
                            first = Character.getNumericValue(instruc[i].charAt(18));
                            second = Character.getNumericValue(instruc[i].charAt(28));
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
                    pass.add(Character.getNumericValue(instruc[i].charAt(14)),pass.remove(Character.getNumericValue(instruc[i].charAt(28))));
                    break;

            }
        }
        for(char c : pass)
            System.out.print(c);

    }

    private static LinkedList<Character> rotateBased(LinkedList<Character> l, int i) {
        LinkedList<Character> list = new LinkedList<>(l);
        if (i > 3)
            i++;
        i++;
        for (int k = 0; k < i; k++)
            list.addFirst(list.removeLast());
        return list;
    }
}

