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
        int t = in.nextInt();
        ArrayList<int[]> list = new ArrayList<int[]>();
        for (int i = 0; i < t; i++) {
            int n = in.nextInt();
            list.add(new int[n]);
            for (int j = 0; j < n; j++)
                list.get(i)[j] = in.nextInt();
        }
        int q = in.nextInt();
        for (int i = 0; i < q; i++) {
            int x = in.nextInt();
            int y = in.nextInt();
            try {
                System.out.println(list.get(x-1)[y-1]);
            }
            catch (IndexOutOfBoundsException e) {
                System.out.println("ERROR!");
            }
        }
    }
}
