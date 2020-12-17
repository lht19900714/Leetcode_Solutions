
# Space: O(n)
# Time: O(n^3)

class Solution:
    def fourSum(self, nums, target):
        if not nums: return []
        if len(nums) < 4: return []

        nums.sort()

        self.res = []
        self.dict = {}

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]: continue
            temp_res_list = self.three_sum(nums[:i] + nums[i + 1:], target - nums[i])
            temp_res_list = list(map(lambda x: x + [nums[i]], temp_res_list))
            self.res += temp_res_list

        for i in self.res:
            temp = tuple(sorted(i))
            self.dict[temp] = 1

        return self.dict.keys()

    def three_sum(self, alist, target):
        res = []
        for i in range(len(alist)):
            if i != 0 and alist[i] == alist[i - 1]: continue
            temp_res_list = self.two_sum(alist[:i] + alist[i + 1:], target - alist[i])
            temp_res_list = list(map(lambda x: x + [alist[i]], temp_res_list))
            res += temp_res_list

        return res

    def two_sum(self, alist, target):
        left, right = 0, len(alist) - 1
        res = []
        while left != right:
            if left >= target: return res
            if alist[left] + alist[right] == target:
                res.append([alist[left], alist[right]])
                right -= 1
            elif alist[left] + alist[right] > target:
                right -= 1
            elif alist[left] + alist[right] < target:
                left += 1
        return res




