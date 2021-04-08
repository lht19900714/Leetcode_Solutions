
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def findItinerary(self, tickets):

        data = collections.defaultdict(list)
        for i, j in tickets:
            data[i].append(j)

        for i, j in data.items():
            j.sort()

        res = []

        def post_order_traversal(ticket):
            temp = data[ticket]  # this is shallow copy, the info in "data" dictionary will be modified.
            while temp:
                cur = temp.pop(0)
                post_order_traversal(cur)
            res.append(ticket)

        post_order_traversal("JFK")
        return res[::-1]



