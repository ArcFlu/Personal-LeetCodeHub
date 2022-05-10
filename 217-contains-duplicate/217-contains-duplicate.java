class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> hashBrown = new HashSet<>();
        for (int num: nums){
            if (!hashBrown.contains(num))
                hashBrown.add(num);
            else
                return true;
        }
        return false;
    }
}