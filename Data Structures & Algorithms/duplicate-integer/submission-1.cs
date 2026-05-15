public class Solution {
    public bool hasDuplicate(int[] nums) {
        Dictionary<int, int> dictMap = new Dictionary<int, int>();
foreach(int num in nums) {
    if (dictMap.ContainsKey(num)) return true;
    dictMap.Add(num, 1);
}
return false;

    }
}
