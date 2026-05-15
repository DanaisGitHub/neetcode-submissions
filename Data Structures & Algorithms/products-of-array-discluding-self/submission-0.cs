public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
         int[] prefix = new int[nums.Length];
 int[] postfix = new int[nums.Length];
 int[] res = new int[nums.Length];

 int i;
 prefix[0] = 1;
 for (i=1; i < nums.Length; i++) {
     prefix[i] = nums[i-1] * prefix[i - 1];
 }
 postfix[nums.Length - 1] = 1;
 for (i = nums.Length-2; i >= 0; i--) {
     postfix[i] = nums[i+1] * postfix[i + 1];
 }

 for (i = 0; i < nums.Length; i++) {
     res[i] = prefix[i] * postfix[i];
 }

 // product of everything / divide itself
 return res;
        
    }
}
