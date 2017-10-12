// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        int n = A.length();
        boolean isPalindrome = true;
        if (n % 2 == 0) {
            for (int i = 0; i < n/2; i++) {
                if (A.charAt(i) != A.charAt(n - 1 - i)) {
                    isPalindrome = false;
                    break;
                }
            }
        }
        else {
            for (int i = 0; i < (n/2)-1; i++) {
                if (A.charAt(i) != A.charAt(n - 1 - i)) {
                    isPalindrome = false;
                    break;
                }                
            }
        }
        if (isPalindrome) System.out.println("Yes");
        else System.out.println("No");
    }
}

