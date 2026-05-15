class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # slidingWindow = set() # CLOSE BUT GOOD
        # setCounter = 0
        # maxWindow = 0

        # for c in s:
        #     if c in slidingWindow:
        #         slidingWindow = set()
        #         setCounter = 0
            
        #     slidingWindow.add(c)
        #     setCounter += 1
        #     maxWindow = max(maxWindow,setCounter)

        # return maxWindow
        maxWindow = 0
        j=0
        slidingWindow = set()

        for i in range(len(s)):
            while s[i] in slidingWindow:
                slidingWindow.remove(s[j])
                j+=1
            slidingWindow.add(s[i])
            maxWindow = max(maxWindow,i-j+1)
        
        return maxWindow

                





            
                


        