
# Space: O(n)
# Time: O(nlogn)

class Solution:
    def findUnsortedSubarray(self, nums):
        length = len(nums)
        if length <= 1: return 0

        cache = sorted(nums)
        left, right = -1, -1

        for i in range(0, length):
            if nums[i] != cache[i]:
                left = i
                break

        if left == -1: return 0

        for j in range(length - 1, -1, -1):
            if nums[j] != cache[j]:
                right = j
                break
                
        return right - left + 1




