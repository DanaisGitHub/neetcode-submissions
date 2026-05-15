import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # add all numbers to the stack,
        # for each operation perform on the last 2 numbers
        # pop the result back into the stack

        stack = []

        operations:dict[str,any] = {
            "*":operator.mul,
            "-":operator.sub,
            "/":operator.truediv,
            "+":operator.add

        }
        

        for token in tokens:
            if not token in operations:
                stack.append(token)
                continue
            yToken = stack.pop()
            xToken = stack.pop()

            result = operations[token](int(xToken), int(yToken))
            stack.append(result)

        return int(stack[-1])



        

        