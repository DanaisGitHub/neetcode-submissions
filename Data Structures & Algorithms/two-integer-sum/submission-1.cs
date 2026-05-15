public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> hashMap = new Dictionary<int,int>();
        int i;
        for (i = 0; i<nums.Length;i++){
            hashMap[nums[i]] = i;
        }
        for (i=0;i<nums.Length;i++){
            int x = target - nums[i];
            if(hashMap.ContainsKey(x) && i != hashMap[x] ){
                return new int[]{i,hashMap[x]};
            }
        }
        return new int[]{0,0};
    }
}
