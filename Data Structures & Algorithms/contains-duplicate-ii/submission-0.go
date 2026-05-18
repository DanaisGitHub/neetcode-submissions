func containsNearbyDuplicate(nums []int, k int) bool {
	abs:=func(num int) int{
		if num<0{
			return num*-1
		}
		return num
	}

	for i,_:=range nums{
		for j := i; j<len(nums);j++{
			if i==j || nums[i] != nums[j]||abs(i-j)>k{
				continue
			}
			return true
		}
	}
	return false

}
