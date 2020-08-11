
# Space: O(n)
# Time: O(n!)

class Solution:
    def permute(self, nums):
        self.res = []
        length = len(nums)

        def backtracking(nums_list, temp_list, length):
            if len(temp_list) == length:
                self.res.append(temp_list[:])
                return

            for index, num in enumerate(nums_list):
                if num in temp_list: continue
                temp_list.append(num)
                new_nums_list = nums_list[:index] + nums[index + 1:]
                backtracking(new_nums_list, temp_list,length)
                temp_list.pop()

        backtracking(nums, [], length)
        return self.res




