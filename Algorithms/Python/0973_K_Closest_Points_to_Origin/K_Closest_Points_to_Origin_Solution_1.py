
# Space: O(1)
# Time: O(n)

class Solution:
    def kClosest(self, points, K):

        points.sort(key=lambda x: (pow(pow(x[0], 2) + pow(x[1], 2), 0.5)))

        return points[:K]



