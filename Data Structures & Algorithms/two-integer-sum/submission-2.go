func twoSum(nums []int, target int) []int {
    	// simple naive j == target - i
	// time = O(n^2)
	// space = O(n)
	for i, num := range nums {
		r := target - num
		// find if r is in nums && index != i
		for j, num2 := range nums {
			if i == j {
				continue
			}
			// within constraints will always be hit
			if r == num2 {
				if j < i {
					return []int{j, i}
				}
				return []int{i, j}
			}
		}

	}
	return []int{}

}
