
# Space: O(n)
# Time: O(n)

class Solution:
    def longestMountain(self, A) -> int:
        length = len(A)
        if length < 3: return 0

        res = 0

        for i in range(1, length - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                left, right = i - 1, i + 1
                left_count, right_count = 0, 0
                while 0 <= left and A[left] < A[left + 1]:
                    left_count += 1
                    left -= 1
                while right < length and A[right] < A[right - 1]:
                    right_count += 1
                    right += 1
                res = max(left_count + right_count + 1, res)

        return res








