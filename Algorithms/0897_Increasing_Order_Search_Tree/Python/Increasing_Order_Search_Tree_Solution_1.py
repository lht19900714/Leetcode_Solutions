
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root):
        if root is None: return root
        if root.left is None and root.right is None: return root

        self.cache = {}
        inorder_node_value = []
        res = TreeNode()
        cur_res = res

        # traverse tree and cache all of them
        queue = [root]
        while queue:
            cur = queue.pop(0)
            self.cache[cur.val] = cur
            inorder_node_value.append(cur.val)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)

        # sort all values
        inorder_node_value.sort()

        # restructure tree
        for i in inorder_node_value:
            cur_res.right = self.cache[i]
            cur_res.left = None
            cur_res = cur_res.right

        # clean up tail node
        cur_res.left = None
        cur_res.right = None

        return res.right




