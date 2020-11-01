
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None or (root.left is None and root.right is None): return root

        # use inorder traversal to find the incorrect node
        inorder_result = self.inorder_traversal(root)
        sorted_inorder_result = sorted(inorder_result)
        node_values = []
        first_node, second_node = 0, 0
        first_flag, second_flag = False, False
        for i, j in zip(inorder_result, sorted_inorder_result):
            if i != j:
                first_node, second_node = i, j
                break

        # use level traversal to loop through tree and update incorrect node
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur.val == first_node and first_flag is False:
                cur.val = second_node
                first_flag = True
            elif cur.val == second_node and second_flag is False:
                cur.val = first_node
                second_flag = True

            if first_flag and second_flag: return

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

    def inorder_traversal(self, root):
        if root is None: return []
        res = []
        res += self.inorder_traversal(root.left)
        res.append(root.val)
        res += self.inorder_traversal(root.right)
        return res



