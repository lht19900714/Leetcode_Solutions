
# Space: O(n)
# Time: O(n)


class Solution:
    def validateStackSequences(self, pushed, popped):
        length = len(pushed)
        if length == 1: return True

        stack = []
        popped_index = 0
        for num in pushed:
            stack.append(num)

            while stack and popped_index < length and popped[popped_index] == stack[-1]:
                stack.pop()
                popped_index += 1

            if popped_index < length and popped[popped_index] in stack: return False

        return True




