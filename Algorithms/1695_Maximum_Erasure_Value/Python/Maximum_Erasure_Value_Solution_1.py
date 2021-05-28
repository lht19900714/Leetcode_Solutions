

# Space: O(n)
# Time: O(n)

class Solution:
    def maximumUniqueSubarray(self, nums):
        length = len(nums)
        if length == 1: return nums[0]
        fast, slow, running_total, res, cache = 0, 0, 0, 0, set()

        while fast < length:
            if nums[fast] in cache:
                res = max(res, running_total)
                running_total -= nums[slow]
                cache.remove(nums[slow])
                slow += 1
            else:
                running_total += nums[fast]
                cache.add(nums[fast])
                fast += 1

        res = max(res, running_total)
        return res





        