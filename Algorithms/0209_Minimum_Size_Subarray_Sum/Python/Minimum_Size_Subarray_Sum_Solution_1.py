
# Space: O(1)
# Time: O(n)

class Solution:
    def minSubArrayLen(self, s, nums):

        length = len(nums)
        if length == 1:
            if nums[0] == s: return 1
            if nums[0] != s: return 0

        slow, fast = 0, 0
        res = length
        temp_sum = 0
        flag = 0

        while slow < length:

            while fast < length and temp_sum < s:
                temp_sum += nums[fast]
                fast += 1

            if temp_sum >= s:
                res = min(res, fast - slow)
                flag = 1

            temp_sum -= nums[slow]
            slow += 1

        return res if flag == 1 else 0




