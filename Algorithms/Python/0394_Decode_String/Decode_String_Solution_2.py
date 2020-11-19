
# Space: O(n)
# Time: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) <= 1: return s

        def get_str(stack):
            res = ''
            while type(stack[-1]) == str:
                res = stack.pop() + res
            return res

        stack = []
        number = 0

        for i in range(len(s)):
            if s[i].isalpha():
                stack.append(s[i])
            elif s[i].isnumeric():
                number = number * 10 + int(s[i])
            elif s[i] == '[':
                stack.append(number)
                number = 0
            elif s[i] == ']':
                temp_res = get_str(stack)
                pop_number = stack.pop()
                stack.append(temp_res * pop_number)

        return ''.join(stack)






