import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        if (s.length() % 2 != 0) {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {

            Character c = (Character) s.charAt(i);
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if ((c == ')' || c == '}' || c == ']') && !stack.empty()) {
                Character top = stack.peek();
                if (top == '(' && c == ')') {
                    stack.pop();
                } else if (top == '{' && c == '}') {
                    stack.pop();
                } else if (top == '[' && c == ']') {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        if (!stack.empty()) {
            return false;
        }
        return true;
    }
}