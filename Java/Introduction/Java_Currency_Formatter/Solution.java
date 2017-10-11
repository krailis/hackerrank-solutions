// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.util.*;
import java.text.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        // Write your code here.
        NumberFormat usFormat = NumberFormat.getCurrencyInstance(Locale.US);
        String us = usFormat.format(payment);
        NumberFormat frFormat = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        String france = frFormat.format(payment);
        NumberFormat chiFormat = NumberFormat.getCurrencyInstance(Locale.CHINA);
        String china = chiFormat.format(payment);
        Locale indy = new Locale("en", "IN");
        NumberFormat inFormat = NumberFormat.getCurrencyInstance(indy);
        String india = inFormat.format(payment);
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}

