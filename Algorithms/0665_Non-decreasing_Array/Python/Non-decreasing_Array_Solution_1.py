
# Space: O(n)
# Time: O(n)

class Solution:
    def checkPossibility(self, nums):
        length = len(nums)
        if length <= 1: return True

        cache = []
        index = 0

        while index < length:
            temp = []
            start_flag = True
            while index < length and (start_flag or nums[index - 1] <= nums[index]):
                temp.append(nums[index])
                start_flag = False
                index += 1
            cache.append(temp)

        if len(cache) <= 1: return True
        if len(cache) > 2: return False
        if len(cache[0]) == 1 or len(cache[1]) == 1: return True
        min_from_array_1 = min(cache[0][-1], cache[0][-2])
        max_from_array_2 = max(cache[1][0], cache[1][1])
        if min_from_array_1 <= cache[1][0]: return True
        if cache[0][-1] <= max_from_array_2: return True
        return False




