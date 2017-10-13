// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh) {
        Scanner in = new Scanner(System.in);
        HashMap<String, Integer> phoneList = new HashMap<String, Integer>();
        
        int n=in.nextInt();
        in.nextLine();
        for(int i=0;i<n;i++) {
            String name=in.nextLine();
            int phone=in.nextInt();
            phoneList.put(name, phone);
            in.nextLine();
        }
        while(in.hasNext()) {
            String s=in.nextLine();
            if (phoneList.containsKey(s)) {
                System.out.println(s + "=" + phoneList.get(s));
            }
            else {
                System.out.println("Not found");
            }
        }
    }
}

