
# Space: O(n)
# Time: O(n^2)

class Solution:
    def fourSumCount(self, A, B, C, D):

        temp = {}
        count = 0
        for i in A:
            for j in B:
                if i + j not in temp:
                    temp[i + j] = 1
                else:
                    temp[i + j] += 1

        for i in C:
            for j in D:
                if -(i + j) in temp:
                    count += temp[-(i + j)]

        return count





