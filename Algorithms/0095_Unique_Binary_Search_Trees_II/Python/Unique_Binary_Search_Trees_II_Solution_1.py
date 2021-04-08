
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n):
        if n == 0: return []

        def recursive(start, end):
            if start > end:
                return [None]

            res_list = []

            for i in range(start, end + 1):
                left = recursive(start, i - 1)
                right = recursive(i + 1, end)

                for each_left in left:
                    for each_right in right:
                        root = TreeNode(i)
                        root.left = each_left
                        root.right = each_right
                        res_list.append(root)
            return res_list

        return recursive(1, n)





