
# Space: O(n)
# Time: O(n!)

class Solution:
    def permute(self, nums):

        def backtracking(nums_list, temp_list, res, visited):
            if temp_list in visited:
                return

            if len(nums_list) == 0:
                res.append(temp_list[:])
                visited.append(temp_list[0])
                return

            for index, num in enumerate(nums_list):
                temp_list.append(num)
                new_nums_list = nums_list[:index] + nums_list[index + 1:]
                backtracking(new_nums_list, temp_list, res, visited)
                visited.append(temp_list[:])
                temp_list.pop()
            return res

        return backtracking(nums, [], [], [])








