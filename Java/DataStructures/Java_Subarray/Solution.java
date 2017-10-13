// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int [] a = new int[n];
        int numOfNegative = 0;
        for (int i = 0; i < n; i++) {
            a[i] = in.nextInt();
            if (a[i] < 0) numOfNegative++;
        }
        in.close();
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j <= n - i; j++) {
                int sum = 0;
                for (int k = j; k < j + i; k++) {
                    sum += a[k];
                }
                if (sum < 0) numOfNegative++;
            }
        }
        System.out.println(numOfNegative);
    }
}
