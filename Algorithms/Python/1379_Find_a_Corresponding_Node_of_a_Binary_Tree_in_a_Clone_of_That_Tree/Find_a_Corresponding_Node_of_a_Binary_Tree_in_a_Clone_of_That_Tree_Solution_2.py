
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        if cloned.left is None and cloned.right is None: return cloned

        queue_original, queue_cloned = [original], [cloned]

        while queue_original:
            cur_original, cur_cloned = queue_original.pop(0), queue_cloned.pop(0)

            if cur_original == target: return cur_cloned

            if cur_original.left:
                queue_original.append(cur_original.left)
                queue_cloned.append(cur_cloned.left)

            if cur_original.right:
                queue_original.append(cur_original.right)
                queue_cloned.append(cur_cloned.right)





