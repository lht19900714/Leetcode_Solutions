
# Space: O(n)
# Time: O(n)

# Solution without collections library


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution():
    def zigzagLevelOrder(self, root):

        queue = [[root, 0]]
        res = []
        temp_res = []
        level_status = 0
        flag = 0
        while queue:
            cur_root, cur_level = queue.pop(0)

            if level_status == cur_level:
                temp_res.append(cur_root.val)
            else:
                level_status = cur_level
                if flag == 0:
                    res.append(temp_res)
                    flag = 1
                else:
                    res.append(temp_res[::-1])
                    flag = 0
                temp_res = [cur_root.val]

            if cur_root.left: queue.append([cur_root.left, cur_level + 1])
            if cur_root.right: queue.append([cur_root.right, cur_level + 1])

        if flag == 0:
            res.append(temp_res)
        else:
            res.append(temp_res[::-1])

        return res

