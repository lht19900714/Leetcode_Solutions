
# Space: O(n)
# Time: O(n)


class Solution:
    def insert(self, intervals, newInterval):

        length = len(intervals)
        if length == 0: return [newInterval]

        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        if intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals
        left, right = [], []
        temp_interval = newInterval[:]
        for i in range(length):
            if intervals[i][1] < newInterval[0]:
                left.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                right.append(intervals[i])
            else:
                temp_interval[0] = min(intervals[i][0], temp_interval[0])
                temp_interval[1] = max(intervals[i][1], temp_interval[1])

        return left + [temp_interval]+ right




