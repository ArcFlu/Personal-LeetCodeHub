class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        // if a string is odd, then it's impossible to have a correct string
        if (s.length() > 0 && s.length() % 2 == 1)
            return false;
        
        // We only care if the closing brackets are in order, so we 
        // use the stack to keep track of what we should see next
        // if we ever encounter a closing bracket
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '(')
                stack.push(')');
            else if (s.charAt(i) == '{')
                stack.push('}');
            else if (s.charAt(i) == '[')
                stack.push(']');
            else if (stack.isEmpty() || stack.pop() != s.charAt(i))
                return false;
        }
        
        if (stack.isEmpty())
            return true;
        
        return false;
    }
}