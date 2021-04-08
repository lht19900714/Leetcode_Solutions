# Space: O(1)
# Time: O(n)

class Solution:
    def maxDistToClosest(self, seats):
        length = len(seats)
        if length == 2: return 1
        if seats.count(1) == 1:
            return seats.index(1) if seats.index(1) > (length - 1) - seats.index(1) else (length - 1) - seats.index(1)

        slow, fast, res = 0, 1, 0

        while slow < length and fast < length:

            while fast < length and seats[fast] != 1:
                fast += 1

            if seats[slow] == 0:
                res = max(res, fast - slow)
            elif fast == length:
                res = max(res, (fast - 1 - slow))
            else:
                target_seat_index = (slow + fast) // 2
                distance = min(target_seat_index - slow, fast - target_seat_index)
                res = max(res, distance)

            slow = fast
            fast = slow + 1

        return res




