
# Space: O(1)
# Time: O(n)

# same approach as solution 1, compress space complexity from n to 1

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], x[1]))  # customized sort, sort by first value of interval and second value of interval
        last_interval = None
        res = 0

        for interval in intervals:
            if last_interval is None:
                last_interval = interval
            elif last_interval == interval:
                res += 1
                continue
            elif interval[0] < last_interval[1]:  # overlapping situation
                res += 1
                if interval[1] < last_interval[1]:
                    last_interval = interval
                else:
                    continue
            else:
                last_interval = interval

        return res





