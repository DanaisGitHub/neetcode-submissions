class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # f = min(y1,y2) * x
        # l,r 

        maxVol = 0

        l,r=0,len(heights)-1

        while l<r:
            x = r-l
            y = min(heights[l],heights[r])
            print(f'{x}*{y}={x*y}')
            maxVol = max(maxVol,y*x)


            tempL = l
            l = l+1 if heights[l]<=heights[r] else l
            r = r-1 if heights[tempL]>heights[r] else r

        
        return maxVol

        