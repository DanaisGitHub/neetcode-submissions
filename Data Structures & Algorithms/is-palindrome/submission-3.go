func isPalindrome(s string) bool {
	s = strings.ToLower(s)
	l,r:=0,len(s)-1

	for l<r{
		if !isAlphaNumeric(byte(s[l])){
			l++
			continue
		}
		if !isAlphaNumeric(byte(s[r])){
			r--
			continue
		}

	if s[l] != s[r]{
		return false
	} 
	l++
	r--
	}
	return true



}

func isAlphaNumeric(c byte) bool{
	return (c >= 'a' && c <= 'z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')
}

