
# Space: O(n)
# Time: O(n)

class Solution:
    def canVisitAllRooms(self, rooms):
        length = len(rooms)
        if length <= 1: return True
        res = set()
        queue = rooms[0]

        while queue:
            cur_key = queue.pop(0)
            if cur_key not in res:
                queue += rooms[cur_key]
                res.add(cur_key)

        for i in range(1, length):
            if i not in res: return False

        return True




