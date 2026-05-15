func hasDuplicate(nums []int) bool {
    return containsDuplicate(nums)
}

func containsDuplicate[T comparable](nums []T) bool {
	hashSet := map[T]any{}

	for _, val := range nums {
		_, found := hashSet[val]
		if found {
			return true
		}
		hashSet[val] = nil
	}
	return false
}