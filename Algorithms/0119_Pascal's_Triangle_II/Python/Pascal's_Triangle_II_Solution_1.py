
# Space: O(n)
# Time: O(n^2)

# same approach as solution 1, compress space from n^2 to n

class Solution:
    def getRow(self, rowIndex):
        data = [1 for _ in range(rowIndex + 1)]

        for i in range(rowIndex + 1):
            temp = data[:]
            for j in range(i):
                if j == 0:
                    continue
                else:
                    data[j] = temp[j] + temp[j - 1]

        return data



