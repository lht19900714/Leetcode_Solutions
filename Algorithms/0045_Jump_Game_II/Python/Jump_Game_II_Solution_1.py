
# Space: O(n)
# Time: O(n)

class Solution:
    def jump(self, nums):
        length = len(nums)
        if length <= 1: return 0
        cache = [0 for _ in range(length)]

        for i in range(length):
            if nums[i] == 0: continue
            for j in range(i + 1, i + 1 + nums[i]):
                if j >= length: break
                cache[j] = cache[i] + 1 if cache[j] == 0 else cache[j]

        return cache[-1]





