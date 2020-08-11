
# Space: O(n)
# Time: O(n!)

class Solution:
    def permuteUnique(self, nums):

        def backtracking(nums_list, temp_list, res, visited):
            if len(nums_list) == len(temp_list):
                res.append(temp_list[:])

            for i, num in enumerate(nums_list):
                if visited[i]: continue
                if i > 0 and nums_list[i] == nums_list[i - 1] and not visited[i - 1]: continue

                temp_list.append(num)
                visited[i] = True
                backtracking(nums_list, temp_list, res, visited)
                temp_list.pop()
                visited[i] = False

            return res

        nums.sort()
        visited = [False for _ in range(len(nums))]

        return backtracking(nums, [], [], visited)



