
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

        start_index, end_index = 0, 0
        for i in range(length):
            if intervals[i][0] <= newInterval[0] <= intervals[i][1] or newInterval[0] < intervals[i][0]:
                start_index = i

                for j in range(i, length):
                    if newInterval[1] < intervals[j][0]:
                        end_index = j
                        temp_interval = [min(intervals[start_index][0], newInterval[0]), newInterval[1]]
                        return intervals[:start_index] + [temp_interval] + intervals[end_index:]

                    if intervals[j][0] <= newInterval[1] <= intervals[j][1] or (j != length - 1 and newInterval[1] < intervals[j + 1][0]):
                        end_index = j
                        temp_interval = [min(intervals[start_index][0], newInterval[0]), max(intervals[j][1], newInterval[1])]
                        return intervals[:start_index] + [temp_interval] + intervals[end_index + 1:]

                    if j == length - 1:
                        temp_interval = [min(intervals[start_index][0], newInterval[0]), max(intervals[j][1], newInterval[1])]
                        return intervals[:start_index] + [temp_interval]





