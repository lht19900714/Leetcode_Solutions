
# Space: O(n)
# Time: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head):
        if head is None: return None

        data = {}
        cur = head

        # create new nodes and save in dict
        while cur:
            data[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        # loop through each node again and link new nodes together
        while cur:
            data[cur].next = data[cur.next] if cur.next else None
            data[cur].random = data[cur.random] if cur.random else None
            cur = cur.next

        return data[head]





