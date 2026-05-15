func validPalindrome(s string) bool {
	if len(s)<=1{
		return true
	}
	for i := range len(s)-1{
		sBy1 := s[:i]+s[i+1:]
		fmt.Println(sBy1)
		if isPalindrome(sBy1){
			return true
		}
	}
	return false
}



func isPalindrome(s string) bool{
	l,r:=0,len(s)-1

	for l < r {
		for l<r && !isAlphaNumeric(s[l]){
			l++
		}
		for r>l && !isAlphaNumeric(s[r]){
			r--
		}
		if s[l] != s[r]{
			return false
		}
		l++
		r--
	}
	return true
}

func isAlphaNumeric [T byte|rune] (c T) bool{
	return (c>='a' && c<='z') || (c>='0' && c<='9')
}
