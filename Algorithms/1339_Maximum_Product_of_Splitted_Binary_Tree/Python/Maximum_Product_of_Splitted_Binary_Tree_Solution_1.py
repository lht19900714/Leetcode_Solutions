
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root):
        cache = {}
        self.res = 0
        mod = 1000000007

        def dfs(root):
            if root is None: return 0
            if root in cache: return cache[root]
            left = dfs(root.left)
            right = dfs(root.right)
            cache[root] = root.val + left + right
            return cache[root]

        dfs(root)

        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur.left:
                self.res = max(self.res, (cache[root] - cache[cur.left]) * cache[cur.left])
                queue.append(cur.left)
            if cur.right:
                self.res = max(self.res, (cache[root] - cache[cur.right]) * cache[cur.right])
                queue.append(cur.right)
        return self.res % mod




