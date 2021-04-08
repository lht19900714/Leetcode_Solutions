
# Space: O(1)
# Time: O(n^2)

class Solution:
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)
        if length == 1:
            return 0 if gas[0] >= cost[0] else -1

        start_index = []
        for i in range(length):
            if gas[i] >= cost[i]:
                start_index.append(i)

        for index in start_index:
            res = self.verify(index, length, gas, cost)
            if res != -1: return res

        return -1

    def verify(self, index, length, gas, cost):
        res = index
        cur_cost, cur_tank = 0, 0
        count = 0

        while count != length + 1:

            if count != 0:
                cur_tank -= cur_cost
                if cur_tank < 0: return -1

            cur_cost = cost[index]
            cur_tank += gas[index]
            index = (index + 1) % length
            count += 1

        return res




