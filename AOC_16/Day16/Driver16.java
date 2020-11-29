/**
 * Created by evanphoward on 3/31/17.
 */

public class Driver16 {
    private static final int LENGTH = 35651584;
    private static final String INPUT = "10001110011110000";
    public static void main(String [] args) {

        String output = driveData(INPUT,LENGTH);

        System.out.print(driveChecksum(output));


    }
    private static String driveChecksum(String input) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < input.length(); i+=2) {
            sb.append(input.charAt(i) == input.charAt(i + 1) ? '1' : '0');
        }

        String checksum = sb.toString();

        if(checksum.length() % 2 == 0) {
            checksum = driveChecksum(checksum);
        }

        return checksum;

    }
    public static String driveData(String a, int driveLength) {

        String b = new StringBuffer(a).reverse().toString();

        b = b.replace('0', 'x');
        b = b.replace('1', '0');
        b = b.replace('x', '1');

        String toReturn = a + '0' + b;

        if(toReturn.length() < driveLength) {
            toReturn = driveData(toReturn, driveLength);
        }

        toReturn = toReturn.substring(0, driveLength);

        return toReturn;

    }
}
