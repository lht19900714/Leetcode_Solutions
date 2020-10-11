
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def removeDuplicates(self, nums) -> int:
        counter = collections.Counter(nums)
        index = 0
        for num in counter:
            if counter[num] > 2:
                temp_count = 2
                while temp_count > 0:
                    nums[index] = num
                    index += 1
                    temp_count -= 1
            else:
                while counter[num] > 0:
                    nums[index] = num
                    index += 1
                    counter[num] -= 1

        return index





