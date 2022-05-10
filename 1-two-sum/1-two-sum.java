class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashBrown = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            hashBrown.put(nums[i], i);
        }
        
        for (int i = 0; i < nums.length; i++){
            int subTarget = target - nums[i];
            if (hashBrown.containsKey(subTarget)){
                if (hashBrown.get(subTarget) == i)
                    continue;
                
                int[] returnArray = new int[2];
                returnArray[0] = i;
                returnArray[1] = hashBrown.get(subTarget);
                return returnArray;
            }
        }
        return null;
    }
}