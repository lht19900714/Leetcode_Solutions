
# Space: O(n)
# Time: O(n)

class Solution:
    def openLock(self, deadends, target):
        if target in deadends or '0000' in deadends: return -1
        deadends = set(deadends)

        queue = [('0000', 0)]
        while queue:
            cur_number, cur_step = queue.pop(0)
            if cur_number == target: return cur_step
            for i in range(4):
                temp_number = int(cur_number[i])
                temp1 = cur_number[:i] + str((temp_number + 1) % 10) + cur_number[i + 1:]
                temp2 = cur_number[:i] + str((temp_number - 1) % 10) + cur_number[i + 1:]
                if temp1 not in deadends:
                    queue.append((temp1, cur_step + 1))
                    deadends.add(temp1)
                if temp2 not in deadends:
                    queue.append((temp2, cur_step + 1))
                    deadends.add(temp2)
        return -1






