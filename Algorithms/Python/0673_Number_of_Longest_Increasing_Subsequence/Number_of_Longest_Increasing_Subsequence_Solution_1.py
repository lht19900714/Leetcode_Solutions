
# Space: O(n)
# Time: O(n)

class Solution():
    def findNumberOfLIS(self, nums):
        nums_length = len(nums)
        if nums_length <= 1: return nums_length

        length = [0] * nums_length  # longest sequence length at length[i]
        count = [1] * nums_length  # count of longest sequence length at count[i]

        for i in range(nums_length):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j] >= length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_length = max(length)

        return sum([count[i] for i in range(nums_length) if length[i]==max_length])





