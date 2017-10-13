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
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < n; i++)
            list.add(in.nextInt());
        int numberOfQueries = in.nextInt();
        for (int i = 0; i < numberOfQueries; i++) {
            String query = in.next();
            if (query.compareTo("Insert") == 0)
                list.add(in.nextInt(), in.nextInt());
            if (query.compareTo("Delete") == 0)
                list.remove(in.nextInt());
        }
        for (int element : list)
            System.out.print(element + " ");
    }
}

