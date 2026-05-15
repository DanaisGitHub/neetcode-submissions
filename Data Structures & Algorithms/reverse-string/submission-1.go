func reverseString(s []byte) {
	// p1 = x, p2 = len(s)-x
	// temp = p1, p1 = p2, p2 = temp
	// do for len(x)/2 || p1<p2
	if len(s) <=1{
		return 
	}
	lp := 0
	rp :=len(s)-1
	temp := s[lp]
	for true{
		if s[lp] == s[rp]{
			lp++
			rp--
			if lp >= rp{
				return
		}
			continue
		}
		temp = s[lp]
		s[lp] = s[rp]
		s[rp] = byte(temp)

		lp++
		rp--
		if lp >= rp{
			return
		}
	}
}
