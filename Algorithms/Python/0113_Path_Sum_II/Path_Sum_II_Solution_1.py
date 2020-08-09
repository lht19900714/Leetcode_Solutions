
# Space: O(n)
# Time: O(n)

# DFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, sum):

        def dfs(root, current_path, target_sum, res):
            if root is None: return

            current_path.append(root.val)

            if root.left is None and root.right is None and root.val == target_sum:
                res.append(current_path)

            # caution: make sure to use deep copy(current_path[:]) instead of shallow copy
            #          otherwise the current_path will include all traversed node.
            dfs(root.left, current_path[:], target_sum - root.val, res)
            dfs(root.right, current_path[:], target_sum - root.val, res)

            return res

        return dfs(root, [], sum, [])



