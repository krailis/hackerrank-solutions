// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.math.*;

class ZeroException extends Exception {
    String str1;
    
    ZeroException(String str2) {
        str1 = str2;
    }
    
    public String toString() {
        return str1;
    }
    
}

class NegativeException extends Exception {
    String str1;
    
    NegativeException(String str2) {
        str1 = str2;
    }
    
    public String toString() {
        return str1;
    }
    
}

class MyCalculator {
    /*
    * Create the method long power(int, int) here.
    */
    public static long power (int a, int b) throws Exception {
        if (a == 0 && b == 0){
            throw new ZeroException("java.lang.Exception: n and p should not be zero.");
        }
        if (a < 0 || b < 0) {
            throw new NegativeException("java.lang.Exception: n or p should not be negative.");
        }
        long base = a;
        long pow = b;
        long product = 1;
        for (int i = 1; i <= pow; i++) {
            product *= base;
        }
        return product;
    }
    
}

