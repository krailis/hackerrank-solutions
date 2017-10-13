// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import static java.lang.System.in;

class Prime {
    public static void checkPrime (int... numbers) {
        for (int n : numbers) {
            BigInteger b = BigInteger.valueOf(n);
            if (b.isProbablePrime(100))
                System.out.print(n + " ");
        }
        System.out.println();
    }
}

