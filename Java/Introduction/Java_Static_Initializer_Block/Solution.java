// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static int B, H;
    public static boolean flag;

    static {
        Scanner scan = new Scanner(System.in);
        B = scan.nextInt();
        H = scan.nextInt();
        flag = false;
        scan.close();
        if (B <= 0 || H <= 0)
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        else
            flag = true;
    }

    public static void main(String[] args){
	if(flag){
	    int area=B*H;
	    System.out.print(area);
	}
    }//end of main
}//end of class

