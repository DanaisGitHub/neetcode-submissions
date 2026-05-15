class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 0 :
            return False
        if len(triplets) == 1:
            target == triplets[0]

        removeArray = []
        for i in range(len(triplets)):
            for j in range(len(triplets[i])):
                if triplets[i][j] > target[j]:
                    removeArray.append(i)
                    break

        removeArray.sort(reverse = True)

        for index in removeArray:
            triplets.pop(index)
        
        if len(triplets) == 0 :
            return False
        if len(triplets) == 1:
            return target == triplets[0]

        maxArray = triplets[0]
        for i in range(len(triplets)):
            for j in range(len(triplets[i])):
                maxArray[j] = max(maxArray[j],triplets[i][j])

        print(maxArray)

        return target == maxArray
        
        

        