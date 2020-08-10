# Space: O(n)
# Time: O(n)

class Solution:
    def nextGreaterElement(self, nums1, nums2):

        next_greater_dict = {}
        stack = []

        # loop through nums2 to build next_greater_dict by using stack.
        # key = each element in nums2
        # value = next greater number for given key.
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater_dict[stack[-1]] = num
                stack.pop()
            stack.append(num)

        # loop through nums1, if item in next_greater_dict then return corresponded value, else -1
        for i in range(len(nums1)):
            nums1[i] = next_greater_dict.get(nums1[i], -1)

        return nums1



