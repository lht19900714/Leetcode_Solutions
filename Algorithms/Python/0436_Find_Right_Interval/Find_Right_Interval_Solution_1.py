# Space: O(n)
# Time: O(nlogn)

import collections


class Solution:
    def findRightInterval(self, intervals):
        self.data = collections.defaultdict(list)
        res = []

        # memorize all start points and it's index
        for index, item in enumerate(intervals):
            self.data[item[0]].append(index)

        # put all start points in a list and sort it, prepare for binary search
        all_start_points = [item[0] for item in intervals]
        all_start_points.sort()

        for index, item in enumerate(intervals):
            start_point = self.binary_search(all_start_points, item[1])

            # if there is no valid result, then append -1
            if start_point is None:
                res.append(-1)
                continue
            # if there is a valid result, then find closest start point.
            res_index = min(self.data[start_point], key=lambda x: abs(x - index))
            res.append(res_index)

        return res

    def binary_search(self, alist, target):
        # this customized binary search will find if any item in the alist is equal to or smallest item that bigger than target

        left, right = 0, len(alist) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if alist[mid] == target:
                left = mid
            elif alist[mid] < target:
                left = mid + 1
            elif alist[mid] > target:
                right = mid

        if alist[left] >= target:
            return alist[left]
        if alist[right] >= target:
            return alist[right]

        return None



