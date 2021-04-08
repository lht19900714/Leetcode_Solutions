
# Space: O(n)
# Time: O(n^2)

class Solution:
    def generate(self, numRows):
        res = []
        prev = []

        for i in range(1, numRows + 1):
            temp = []
            for j in range(i):
                if j == 0 or j >= len(prev):
                    temp.append(1)
                else:
                    temp.append(prev[j] + prev[j - 1])
            res.append(temp)
            prev = temp[:]
        return res



