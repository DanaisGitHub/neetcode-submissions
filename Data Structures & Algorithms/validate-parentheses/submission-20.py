class Solution:
    def isValid(self, s: str) -> bool:
        # if there exsits even 1 ] without a [before it the solution is wrong
        stack = []
        bracketMap = {
        '}':'{',
        ']':'[',
        ')':'('
        }


        for c in s:
    
            if c in bracketMap:
                if stack and stack[-1] == bracketMap[c]:
                    stack.pop()
                else:
                    return False
                continue

            stack.append(c)

        return True if not stack else False

                

        