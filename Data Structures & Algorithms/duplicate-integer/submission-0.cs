

public class Solution {
    public bool hasDuplicate(int[] nums) {
        // sort then check
        // add to hashmap then check
        HashSet<int> hashset = new HashSet<int>();

        int i = 0;
        for (i=0;i<nums.Length;i++){
            hashset.Add(nums[i]);
        }

        if (hashset.Count == nums.Length){
            return false;
        }
        return true;

    }
}
