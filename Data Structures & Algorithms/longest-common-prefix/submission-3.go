func longestCommonPrefix(strs []string) string {
	// pointer at each str
	// only increment when i for all strs is the same
	// if so next char
	// else return
	if len(strs) ==1{
		return strs[0]
	}
	findMinWordLen := func(strs []string) int {
		min := len(strs[0])

		for _, str := range strs {
			if min > len(str) {
				min = len(str)
			}
		}
		return min
	}

	minWordLen := findMinWordLen(strs)
	ans := ""
	strsLen := len(strs) - 1

	for i := range minWordLen {

		for j := range strsLen {
			wordA := strs[j]
			wordB := strs[j+1]

			if wordA[i] != wordB[i] {
				return ans
			}
			if j == strsLen-1 {
				ans = fmt.Sprint(ans, string(wordA[i]))
			}
		}
	}
	return string(ans)
}
