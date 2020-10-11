
# Space: O(1)
# Time: O(n)


class Solution:
    def removeDuplicates(self, nums) -> int:
        length = len(nums)

        slow, fast, count = 0, 1, 1

        while fast < length:
            if nums[fast] == nums[slow] and count < 2:
                slow += 1
                nums[slow] = nums[fast]
                count += 1
            elif slow > 0 and nums[fast] == nums[slow - 1] and count < 2:
                nums[slow] = nums[fast]
                slow += 1
                count += 1
            elif nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                count = 1
            fast += 1
        return slow + 1



