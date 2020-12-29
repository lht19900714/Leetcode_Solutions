
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution:
    def pseudoPalindromicPaths(self, root):
        if root.left is None and root.right is None: return 1

        self.res = []
        self.count = 0

        def generate_path(root, temp_res):
            temp_res.append(root.val)
            if root.left is None and root.right is None:
                self.res.append(temp_res[:])
                return
            if root.left:
                generate_path(root.left, temp_res)
                temp_res.pop()
            if root.right:
                generate_path(root.right, temp_res)
                temp_res.pop()

        def verify_res(alist):
            odd_flag = False
            temp = collections.Counter(alist)
            for key, value in temp.items():
                if value % 2 != 0:
                    if odd_flag is False:
                        odd_flag = True
                    else:
                        return False
            return True

        generate_path(root, [])
        for each_res in self.res:
            self.count += 1 if verify_res(each_res) else 0

        return self.count




