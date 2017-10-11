// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.math.BigDecimal;
import java.util.*;

class Solution{

    public static void main(String []args){
        //Input
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        String []s=new String[n+2];
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
      	sc.close();

        //Write your code here
        BigDecimal[] a = new BigDecimal[n];
        for (int i = 0; i < n; i++) {
            a[i] = new BigDecimal(s[i]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < (n - i); j++) {
                if (a[j - 1].compareTo(a[j]) < 0) {
                    BigDecimal temp = a[j - 1];
                    a[j - 1] = a[j];
                    a[j] = temp;
                    String temp2 = s[j - 1];
                    s[j - 1] = s[j];
                    s[j] = temp2;
                }
            }
        }
	//Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }
    }
}
