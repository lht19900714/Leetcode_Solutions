
# Space: O(n)
# Time: O(logn)

class Solution:
    def findClosestElements(self, arr, k, x):
        length = len(arr)
        if length == 0: return []
        if length == k: return arr
        res = []

        while k:
            target_index = self.binary_search(arr, x)
            res.append(arr[target_index])
            arr.pop(target_index)
            k -= 1
        return sorted(res)

    def binary_search(self, alist, target):
        left, right = 0, len(alist) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if alist[mid] == target:
                return mid
            if alist[mid] < target:
                left = mid
            elif alist[mid] > target:
                right = mid

        if abs(target - alist[left]) > abs(target - alist[right]):
            return right

        return left




