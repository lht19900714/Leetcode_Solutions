
# Space: O(1)
# Time: O(n)


class Solution:
    def intervalIntersection(self, firstList, secondList):
        if not firstList or not secondList: return []
        i = j = 0
        res = []

        while i < len(firstList) and j < len(secondList):
            left = max(firstList[i][0], secondList[j][0])
            right = min(firstList[i][1], secondList[j][1])
            if left <= right: res.append([left, right])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res





