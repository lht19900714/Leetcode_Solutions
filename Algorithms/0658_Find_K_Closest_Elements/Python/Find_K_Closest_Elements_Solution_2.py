
# Space: O(n)
# Time: O(n)

class Solution:
    def findClosestElements(self, arr, k, x):
        length = len(arr)
        if k >= length: return arr
        sorted_arr = sorted(arr, key=lambda temp: abs(temp - x))
        return sorted(sorted_arr[:k])





