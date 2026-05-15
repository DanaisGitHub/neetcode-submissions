public class Solution {

        public string Encode(IList<string> strs) {
            string res = "";

            foreach ( string s in strs) {
                int num = s.Length;
                res += $"{num}#{s}";
            }

            return res;
        } 

        public List<string> Decode(string s) {
            if (s == ""){
                return new List<string> ();
            }
            List<string> res = new List<string>();

            int i=0;
            int endNum = i;
            do {
                endNum = i;
                while (s[endNum] !='#') {
                    endNum++;
                    
                }
                int nextWordLength = int.Parse(s.Substring(i,endNum - i));
                int end = nextWordLength;
               
                Console.WriteLine(s.Substring(endNum+1, end));
                
                res.Add(s.Substring(endNum+1 , end));
                i += nextWordLength + (endNum - i)+1;
            } while (i < s.Length);

            return res;
        } 
}
