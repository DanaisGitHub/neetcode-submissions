public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
                    List<List<string>> res = new();
Dictionary<string, List<string>> dictMap = new ();


foreach (string str in strs) {
    int[] alpha = new int[26]; // all values = 0
    
    
    foreach (char s in str) {
        alpha[s - 'a']++;
    }

    string strAlpha = string.Join(",", alpha); // when you join as string 10 and 01 look the same
    if (!dictMap.ContainsKey(strAlpha)) {
        dictMap.Add(strAlpha, new List<string>());
    }
    Console.WriteLine(strAlpha);
    dictMap[strAlpha].Add(str);
       
}

foreach (KeyValuePair<string, List<string>> anagrams in dictMap) {
    Console.WriteLine($"[{anagrams}] = {string.Join(",", anagrams.Value)}");
}



    foreach (KeyValuePair<string, List<string>> anagrams in dictMap) {

    res.Add(anagrams.Value);
}
Console.WriteLine($" ----------- FUNCTION END  ----------- ");

return res;
        }
    
}
