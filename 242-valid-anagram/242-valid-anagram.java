class Solution {
    public boolean isAnagram(String s, String t) {
        int[] alphaArray = new int[26];
        int[] betaArray = new int[26];

        for (int i = 0; i < s.length(); i++){
            int charToInt = s.charAt(i) - 'a';
            alphaArray[charToInt] += 1;
        }
        
        for (int i = 0; i < t.length(); i++){
            int charToInt = t.charAt(i) - 'a';
            betaArray[charToInt] += 1;
        }
        
        for (int i = 0; i < 26; i++){
            if (alphaArray[i] != betaArray[i])
                return false;
        }
        return true;
    }
}