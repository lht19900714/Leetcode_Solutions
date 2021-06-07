
# Space: O(1)
# Time: O(n)

class Solution:

    def minCostClimbingStairs(self, cost):
        length = len(cost)
        if length <= 2: return min(cost)
        temp_1, temp_2, temp_3 = 0, 0, 0
        for i in range(2, length + 1):
            temp_3 = min(temp_2 + cost[i - 1], temp_1 + cost[i - 2])
            temp_1, temp_2 = temp_2, temp_3

        return temp_3




