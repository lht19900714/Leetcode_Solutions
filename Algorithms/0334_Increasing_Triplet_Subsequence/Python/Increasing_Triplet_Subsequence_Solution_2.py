
# Space: O(1)
# Time: O(n^2)

class Solution:
    def increasingTriplet(self, nums):
        self.flag = False

        def backtracking(nums, index, temp_res, counter):
            if counter == 3:
                self.flag = True
                return

            for i in range(index, len(nums)):
                if not temp_res or temp_res[-1] < nums[i]:
                    temp_res.append(nums[i])
                    counter += 1
                    backtracking(nums, i + 1, temp_res, counter)
                    if self.flag: return True
                    counter -= 1
                    temp_res.pop()

        return backtracking(nums, 0, [], 0)




