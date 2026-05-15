class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        j = 0

        for i in range(1,len(prices)):
            maxProfit = max(maxProfit,prices[i] - prices[j])

            if prices[i] < prices[j]:
                j = i
        
        return maxProfit

            

        