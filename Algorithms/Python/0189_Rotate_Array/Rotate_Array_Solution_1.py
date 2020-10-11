
# Space: O(1)
# Time: O(n)

class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k == 0: return
        length = len(nums)
        if length <= 1: return

        for i in range(k):
            nums.insert(0,nums.pop())




