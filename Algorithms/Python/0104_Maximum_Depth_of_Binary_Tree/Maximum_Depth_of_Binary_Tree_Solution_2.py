
# Space: O(1)
# Time: O(n)

# Iterative approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0

        level = 1
        temp = [[root ,level]]
        result = 0

        while temp:
            cur = temp.pop()
            result = max(result ,cur[1])
            if cur[0].left:
                temp.append([cur[0].left ,cur[1 ] +1])
            if cur[0].right:
                temp.append([cur[0].right ,cur[1 ] +1])

        return result




