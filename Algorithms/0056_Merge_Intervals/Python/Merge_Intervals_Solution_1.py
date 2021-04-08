
# Space: O(1)
# Time: O(n)


class Solution:
    def merge(self, intervals):

        length = len(intervals)
        if length <= 1: return intervals

        intervals.sort(key=lambda x: (x[0], x[1]))
        res = []

        for i in range(length):
            if len(res) == 0:  res.append(intervals[i])

            elif intervals[i][0] > res[-1][1]:
                res.append(intervals[i])

            elif intervals[i][0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(intervals[i][1], res[-1][1])]

        return res





