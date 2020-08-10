
# Space: O(n)
# Time: O(n)

class Solution:
    def nextGreaterElements(self, nums):
        length = len(nums)
        length_temp_nums = length * 2  # double original array length to simulate circular array
        res = [-1] * length  # initial result array
        stack = []

        for i in range(length_temp_nums):
            while stack and nums[i % length] > nums[stack[-1]]:  # "i % length" is the important part to keep the index with in the original array
                res[stack[-1]] = nums[i % length]
                stack.pop()
            if i < length:  # only put valid index into stack
                stack.append(i)
        return res


