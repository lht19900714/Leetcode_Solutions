
# Space: O(n)
# Time: O(n)

class Solution:
    def longestMountain(self, A) -> int:
        length = len(A)
        if length < 3: return 0

        left = [1 for _ in range(length)]
        right = [0 for _ in range(length)]
        res = 0

        for i in range(1, length - 1):
            if A[i] > A[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(length - 2, -1, -1):
            if A[i] > A[i + 1]:
                right[i] = right[i + 1] + 1

        for i, j in zip(left, right):
            if i != 1 and j != 0:
                res = max(res, i+j)

        return res




