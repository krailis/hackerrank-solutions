// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int sum_b = a + b;
            int pow_b = b;
            System.out.print(sum_b + " ");
            for (int j = 1; j < n; j++) {
                pow_b *= 2;
                sum_b += pow_b;
                System.out.print(sum_b + " ");
            }
            System.out.println();
        }
        in.close();
    }
}

