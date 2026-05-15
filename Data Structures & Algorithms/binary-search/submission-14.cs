public class Solution {
    public int Search(int[] nums, int target) {
                    // do a binary search

          // do a binary search

          int l, r, m;
          l = 0;
          r = nums.Length - 1;

          while (r >= l) {
              m = (l + r) / 2;
              if (target == nums[m]) return m;

              if (target > nums[m]) l = m + 1; // can't be m so step over m( you make the circle smaller 

              if (target < nums[m]) r = m -1;

          } 

          return -1;
      }


        

        
    
}
