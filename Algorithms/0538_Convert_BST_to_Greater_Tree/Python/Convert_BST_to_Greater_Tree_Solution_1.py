
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root):
        if (root is None) or (root.left is None and root.right is None): return root

        def inorder_traversal(root):
            if root is None: return []
            res = []
            left = inorder_traversal(root.left)
            res.append(root.val)
            right = inorder_traversal(root.right)
            return left + res + right

        def update_BST(adict, root):
            queue = [root]
            while queue:
                cur = queue.pop(0)
                # print(cur.val)
                cur.val = adict[cur.val]
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            return root

        inorder_traversal_res = inorder_traversal(root)
        cache = {}
        for i in range(len(inorder_traversal_res)):
            cache[inorder_traversal_res[i]] = sum(inorder_traversal_res[i:])

        return update_BST(cache, root)




