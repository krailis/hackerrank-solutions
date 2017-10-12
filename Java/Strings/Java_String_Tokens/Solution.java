// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        if (scan.hasNext()) {
            String s = scan.nextLine();
            scan.close();
            // Write your code here.
            String[] words = s.trim().split("[ !,?._'@]+");
            int n = words.length;
            System.out.println(n);
            for (int i = 0; i < n; i++)
                System.out.println(words[i]);
        }
        else {
            System.out.println(0);
        }
    }   
}

