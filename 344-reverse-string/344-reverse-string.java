class Solution {
    public void reverseString(char[] s) {
        int pointerA = 0;
        int pointerB = s.length - 1;
        
        while (pointerA < pointerB){
            char temp = s[pointerB];
            s[pointerB] = s[pointerA];
            s[pointerA] = temp;
            
            pointerA++;
            pointerB--;
        }
    }
}