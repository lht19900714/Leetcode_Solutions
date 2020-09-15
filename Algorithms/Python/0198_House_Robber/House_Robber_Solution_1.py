
# Space: O(n)
# Time: O(n)

class Solution:
    def rob(self, nums):
        length = len(nums)
        if length == 0: return 0
        if length == 1: return nums[0]
        if length == 2: return max(nums[0], nums[1])

        memory = [0]*length
        memory[0] = nums[0]
        memory[1] = max(nums[0],nums[1])

        for i in range(2,length):
            memory[i] = max(memory[i-1],memory[i-2]+nums[i])

        return memory[-1]





