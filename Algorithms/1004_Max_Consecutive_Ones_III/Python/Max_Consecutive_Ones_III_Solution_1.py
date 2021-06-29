
# Space: O(1)
# Time: O(n)

class Solution:
    def longestOnes(self, nums, k):
        length = len(nums)
        if length == 0: return 0
        if length == 1: return 1 if k >= 1 else 0
        fast, slow, res, count = 0, 0, 0, k
        while fast < length:
            if nums[fast] == 1:
                fast += 1
            elif nums[fast] == 0 and count > 0:
                count -= 1
                fast += 1

            elif count == 0:
                res = max(len(nums[slow:fast]), res)

                while count == 0:
                    if nums[slow] == 0:
                        count += 1
                    slow += 1
        return res




