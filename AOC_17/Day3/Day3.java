package Day3;

import java.io.File;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Created by evanphoward on 12/2/17.
 */
public class Day3 {
      private static final int VAR = 312051;
      public static void main(String[] args) throws Exception {
         int temp = (int)(Math.sqrt(VAR));
         int[][] arr = new int[temp][temp];
         int x = arr.length/2,y=arr.length/2;
         arr[x][y]=1;
         x+=1;
         for(int i=0;i<=VAR;i++) {
            int thing = arr[x+1][y]+arr[x-1][y]+arr[x][y-1]+arr[x][y+1]+arr[x-1][y-1]+arr[x+1][y-1]+arr[x+1][y+1]+arr[x-1][y+1];
            arr[x][y]=thing;
            if(arr[x][y]>VAR) {
               System.out.println(arr[x][y]);
               break;
            }
            if(i!=VAR) {
               if (arr[x - 1][y] == 0 && arr[x][y + 1] != 0)
                  x -= 1;
               else if (arr[x + 1][y] != 0 && arr[x][y + 1] == 0)
                  y += 1;
               else if (arr[x + 1][y] == 0 && arr[x][y - 1] != 0)
                  x += 1;
               else
                  y -= 1;
            }
         }
      }
}
