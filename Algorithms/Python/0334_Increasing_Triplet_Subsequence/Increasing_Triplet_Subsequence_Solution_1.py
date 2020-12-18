
# Space: O(1)
# Time: O(n)

class Solution:
    def increasingTriplet(self, nums):
        temp = [float('inf'), float('inf')]

        for i in range(len(nums)):
            if nums[i] < temp[0]: temp[0] = nums[i]
            if temp[0] < nums[i] < temp[1]: temp[1] = nums[i]
            if nums[i] > temp[1]: return True
        return False




