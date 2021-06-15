
# Space: O(1)
# Time: O(n)

class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes = sorted(boxTypes, key=lambda x: (-x[1], x[0]))
        res = 0
        for box, unit in boxTypes:
            if truckSize == 0: return res
            temp = min(box, truckSize)
            res += temp * unit
            truckSize -= temp
        return res




