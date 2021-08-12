
# Space: O(n)
# Time: O(n^2)
import collections


class Solution:
    def canReorderDoubled(self, arr):
        length = len(arr)
        if length == 2:
            return True if arr[0] * 2 == arr[1] or arr[1] * 2 == arr[0] else False
        cache = collections.defaultdict(list)
        res = []
        for i in range(length):
            cache[arr[i]].append(i)

        less_than_zero = [n for n in arr if n < 0]
        greater_than_zero = [n for n in arr if n >= 0]
        less_than_zero = sorted(less_than_zero, reverse=True)
        greater_than_zero = sorted(greater_than_zero)
        arr_copy = less_than_zero + greater_than_zero

        for n in arr_copy:
            target_number = 2 * n
            if n in cache and target_number in cache:
                if cache[n]:
                    res.append(n)
                    cache[n].pop()
                    if not cache[n]: cache.pop(n)
                if cache[target_number]:
                    res.append(target_number)
                    cache[target_number].pop()
                    if not cache[target_number]: cache.pop(target_number)

        return sorted(res) == sorted(arr)




