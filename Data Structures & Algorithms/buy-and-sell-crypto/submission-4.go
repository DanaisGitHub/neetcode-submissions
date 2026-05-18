func maxProfit(prices []int) int {
	// I already knew this q, so you need to buy when prices move up & sell when down

	// sliding comes in buy dyamin your window is consectuive stocks that go up

	// [10,2,3,8,4,1,2] 1+4 = 5 + 1 = 6

	max:=func(x,y int) int{
		if x<y{
			return y
		}
		return x
	}


	l:=0
	maxWinSum := 0 
	for r,_ := range prices{
		if r == 0{
			continue
		}

		if prices[l]<prices[r]{
			maxWinSum = max(maxWinSum,prices[r]-prices[l])
			
		}else{
			l=r
		}
		
	}
	return maxWinSum
}
