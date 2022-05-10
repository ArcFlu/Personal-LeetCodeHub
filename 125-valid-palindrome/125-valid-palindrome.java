class Solution {
    public boolean isPalindrome(String s) {
        // pointer at beginning and at end
        // as we go along, if the character is a letter, we do to lower
        // if the character is not a letter, then we move that pointer along.
        // if the pointers are equal to each other in index and character, then             we find palindrome
        // else not palindrome
        
        int startPointer = 0;
        int endPointer = s.length() - 1;
        
        while (startPointer < endPointer){
            char charA = s.charAt(startPointer);
            char charB = s.charAt(endPointer);
            
            // skip non-alphanumeric characters
            if (!Character.isLetter(charA) && !Character.isDigit(charA)){
                startPointer++;
                continue;
            }
            if (!Character.isLetter(charB) && !Character.isDigit(charB)){
                endPointer--;
                continue;
            }
            
            if (Character.isLetter(charA))
                charA = Character.toLowerCase(charA);
            if (Character.isLetter(charB))
                charB = Character.toLowerCase(charB);
            
            if (charA != charB)
                return false;
            
            startPointer++;
            endPointer--;
        }
        
        return true;
        
    }
}