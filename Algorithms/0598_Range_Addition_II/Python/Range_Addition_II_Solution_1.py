
# Space: O(n)
# Time: O(n)

class Solution:
    def maxCount(self, m, n, ops):
        if not ops: return m * n
        max_row, max_column = ops[0][0], ops[0][1]
        for i, j in ops[1:]:
            max_row = min(max_row, i)
            max_column = min(max_column, j)
        return max_row * max_column





