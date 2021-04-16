
# Space: O(n)
# Time: O(n)

class Solution:
    def removeDuplicates(self, s, k):
        length = len(s)
        if length <= 1: return s
        if k > length: return s

        stack = [['#', 1]]
        for char in s:
            if char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])

            while stack[-1][1] >= k:
                stack[-1][1] -= k
                if stack[-1][1] == 0: stack.pop()

        return ''.join([i[0] * i[1] for i in stack[1:]])













