
# Space: O(n)
# Time: O(n)

class Solution:
    def removeCoveredIntervals(self, intervals):
        length = len(intervals)
        if length == 1: return 1

        intervals.sort(key=lambda x: (x[0], -x[1]))
        stack = []

        for i in range(length):
            stack.append(intervals[i])

            while len(stack) > 1 and stack[-2][0] <= stack[-1][0] <= stack[-1][1] <= stack[-2][1]:
                stack.pop()

        return len(stack)




test  = 'abc'
test.strip()