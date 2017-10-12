// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.util.Scanner;
import java.util.regex.*;

public class Solution
{
   public static void main(String[] args){
      Scanner in = new Scanner(System.in);
      int testCases = Integer.parseInt(in.nextLine());
      while(testCases>0){
          String pattern = in.nextLine();
          boolean invalid = false;
          //Write your code
          try {
              Pattern.compile(pattern);
          }
          catch (PatternSyntaxException e) {
              System.out.println("Invalid");
              invalid = true;
          }
          if (!invalid)
              System.out.println("Valid");
          testCases--;
      }
   }
}

