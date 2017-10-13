// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        BitSet b1 = new BitSet(n);
        BitSet b2 = new BitSet(m);
        while (in.hasNext()) {
            String op = in.next();
            int oprnd1 = in.nextInt();
            int oprnd2 = in.nextInt();
            if (op.compareTo("AND") == 0) {
                if (oprnd1 == 1) b1.and(b2);
                else b2.and(b1);
            }
            else if (op.compareTo("OR") == 0) {
                if (oprnd1 == 1) b1.or(b2);
                else b2.or(b1);
            }
            else if (op.compareTo("XOR") == 0) {
                if (oprnd1 == 1) b1.xor(b2);
                else b2.xor(b1);
            }
            else if (op.compareTo("FLIP") == 0) {
                if (oprnd1 == 1) b1.flip(oprnd2);
                else b2.flip(oprnd2);
            }
            else if (op.compareTo("SET") == 0) {
                if (oprnd1 == 1) b1.set(oprnd2);
                else b2.set(oprnd2);
            }
            System.out.println(b1.cardinality() + " " + b2.cardinality());
        }
    }
}
