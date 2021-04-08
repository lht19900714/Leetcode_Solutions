
# Space: O(1)
# Time: O(n)

class Solution:
    def singleNumber(self, nums):
        res = []
        length = len(nums)
        nums.sort()
        status = 0

        for i in range(length):
            if i == 0:
                if nums[i] != nums[i + 1]:
                    res.append(nums[i])
                    status += 1
            elif i == length - 1:
                if nums[i] != nums[i - 1]:
                    res.append(nums[i])
                    status += 1
            else:
                if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                    res.append(nums[i])
                    status += 1

            if status == 2: return res

        return res


