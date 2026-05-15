public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> hashMap = new Dictionary<int, int>();
 foreach (int num in nums)
 {
     if (hashMap.ContainsKey(num)) hashMap[num]++;
     else hashMap[num] = 1;
 }
 // order the hashmap
 List<int[]> orderedMap = new List<int[]>(); // [key,value]
 orderedMap = hashMap.Select(keyMap => new int[] { keyMap.Key, keyMap.Value }).ToList();//LINQ EXAMPLE
                                                                                        // so orderedMap now is Unordered List 
                                                                                       // Now we need to sort it
 orderedMap.Sort((one, two) => two[1].CompareTo(one[1]));

 int[] res = new int[k];
 int i;
 for (i = 0; i < k; i++)
 {
     res[i] = orderedMap[i][0];
 }
 return res;
        
    }
}
