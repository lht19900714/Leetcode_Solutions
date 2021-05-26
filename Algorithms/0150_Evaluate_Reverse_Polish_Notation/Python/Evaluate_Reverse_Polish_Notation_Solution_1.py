
# Space: O(n)
# Time: O(n)

class Solution:
    def evalRPN(self, tokens):
        length = len(tokens)
        if length == 1 and tokens[0].isdecimal(): return int(tokens[0])
        stack = []
        operators = {'+', '-', '*', '/'}
        for i in tokens:
            if i in operators:
                right = stack.pop()
                left = stack.pop()
                res = str(int(eval(left + i + right)))
                stack.append(res)
            else:
                stack.append(i)
        return int(stack[0])




