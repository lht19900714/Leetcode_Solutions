import random

# Space: O(n)
# Time: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.cache = []
        while head:
            self.cache.append(head.val)
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        """
        return random.choice(self.cache)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()





