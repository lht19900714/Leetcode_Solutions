
# Space: O(n)
# Time: O(n)

# DFS Approach

class Solution:
    def canReach(self, arr, start):
        length = len(arr)
        if length == 1 and start == 0: return True

        self.visited = []

        def helper(index):
            if index in self.visited: return False
            if arr[index] == 0: return True
            left_res, right_res = False, False

            self.visited.append(index)
            if 0 <= index + arr[index] < length: right_res = helper(index + arr[index])
            if 0 <= index - arr[index] < length: left_res = helper(index - arr[index])
            self.visited.pop()

            return left_res or right_res

        return helper(start)



