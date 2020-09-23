
# Space: O(1)
# Time: O(n)

class Solution:
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)
        if length == 1:
            return 0 if gas[0] >= cost[0] else -1

        start_index = 0
        remain_gas = 0
        total_gas = 0

        for i in range(length):
            remain_gas += gas[i] - cost[i]

            if remain_gas < 0:
                start_index = i + 1
                remain_gas = 0

            total_gas += gas[i] - cost[i]

        return start_index if total_gas > 0 else -1




