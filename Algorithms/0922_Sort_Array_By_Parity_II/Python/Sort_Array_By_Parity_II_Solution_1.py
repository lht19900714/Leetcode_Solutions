
# Space: O(n)
# Time: O(n)

class Solution:
    def sortArrayByParityII(self, nums):
        res = [0] * len(nums)
        odd_cur, even_cur = 1, 0
        for num in nums:
            if num % 2 == 0:
                res[even_cur] = num
                even_cur += 2
            else:
                res[odd_cur] = num
                odd_cur += 2
        return res




