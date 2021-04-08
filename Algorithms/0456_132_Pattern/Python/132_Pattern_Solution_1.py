
# Space: O(n)
# Time: O(n)


class Solution:
    def find132pattern(self, nums):
        length = len(nums)
        if length < 3: return False
        stack = []

        min_array = [nums[0]] * length
        for i in range(1, length):
            min_array[i] = min(min_array[i - 1], nums[i])

        for i in range(length - 1, -1, -1):
            if nums[i] == min_array[i]: continue

            while stack and stack[-1] < nums[i]:
                if min_array[i]<stack[-1]< nums[i]:
                    return True
                stack.pop()

            if nums[i] > min_array[i]: stack.append(nums[i])

        return False





