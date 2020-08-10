
# Space: O(n)
# Time: O(n)

# Explanation:
# Monotonic stack approach
# Using stack to save INDEX of temperatures, the stack is in "ascending" order. (lowest temperature in the bottom).
# Loop through each item, when the current temperature is greater than stack top temperature, then start to pop item out
# of stack, and the result(next warmer temperature) of popped item is equal to current temperature index - stack popped item.

class Solution:
    def dailyTemperatures(self, T):
        stack = []
        res = [0] * len(T)  # initial result array
        for i in range(len(T)):

            while stack and T[stack[-1]] < T[i]:  # the current temperature is greater than stack top temperature
                res[stack[-1]] = i - stack[-1]  # result of popped item: current temperature index - stack popped item.
                stack.pop()
            else:
                stack.append(i)
        return res



