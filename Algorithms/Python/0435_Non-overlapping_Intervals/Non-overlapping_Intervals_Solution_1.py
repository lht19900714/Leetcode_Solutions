# Space: O(n)
# Time: O(n)

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], x[1]))  # customized sort, sort by first value of interval and second value of interval
        original_length = len(intervals)
        stack = []

        for interval in intervals:
            if len(stack) == 0:
                stack.append(interval)
            elif stack[-1] == interval:
                continue
            elif interval[0] < stack[-1][1]:  # overlapping situation
                if interval[1] < stack[-1][1]:
                    stack.pop()
                    stack.append(interval)
                else:
                    continue
            else:
                stack.append(interval)
        print(stack)
        return original_length - len(stack)





