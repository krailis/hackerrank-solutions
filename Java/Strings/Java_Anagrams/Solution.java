// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.io.*;
import java.util.*;

public class Solution {

    static boolean isAnagram(String a, String b) {
        //=======================================================================================
        int n = a.length();
        if (n != b.length()) return false;
        String aLowerCase = a.toLowerCase();
        String bLowerCase = b.toLowerCase();
        String temp = new String(aLowerCase);
        for (int i = 0; i < n; i++) {
            int countStringA = n - temp.replaceAll("" + aLowerCase.charAt(i), "").length();
            int countStringB = n - bLowerCase.replaceAll("" + aLowerCase.charAt(i), "").length();
            if (countStringA != countStringB) return false;
        }
        return true;
	//======================================================================================
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
