
# Space: O(1)
# Time: O(n)

class Solution:
    def findMinArrowShots(self, points):
        length = len(points)
        if length == 0: return 0
        if length == 1: return 1

        points.sort(key=lambda x: x[1])


        cur = points[0]
        res = 1

        for i in range(length):
            if cur[1] < points[i][0]:
                res += 1
                cur = points[i]

        return res




