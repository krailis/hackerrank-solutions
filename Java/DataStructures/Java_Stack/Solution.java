// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.util.*;

class Solution{

    public static void main(String []argh) {

        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {
            String input=sc.next();
            int n = input.length();
            Stack stack = new Stack();
            boolean isBalanced = true;

            for (int i = 0; i < n; i++) {
                char current = input.charAt(i);
                if (current == '(' || current == '{' || current == '[')
                    stack.push(current);
                if (current == ')' || current == '}' || current == ']') {
                    if (!stack.isEmpty()) {
                        if ((stack.peek() == '(' && current == ')') || (stack.peek() == '[' && current == ']') || (stack.peek() == '{' && current == '}')) {
                            stack.pop();
                        }
                        else {
                            isBalanced = false;
                            break;
                        }
                    }
                    else {
                        isBalanced = false;
                        break;
                    }
                }
            }
            if ((!stack.isEmpty()) || (!isBalanced)) System.out.println("false");
            else System.out.println("true");
        }
    }
}
