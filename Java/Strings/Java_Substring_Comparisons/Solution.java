// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
//=================================================================================
    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "z";
        String largest = "a";
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        int n = s.length();
        if (k == n) return s + "\n" + s;
        for (int i = 0; i < n- k + 1; i++) {
            String subStr = s.substring(i, i + k);
            if (smallest.compareTo(subStr) > 0) {
                smallest = subStr;
            }
            if (largest.compareTo(subStr) < 0) {
                largest = subStr;
            }
        }
        
        return smallest + "\n" + largest;
    }
//================================================================================
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}

