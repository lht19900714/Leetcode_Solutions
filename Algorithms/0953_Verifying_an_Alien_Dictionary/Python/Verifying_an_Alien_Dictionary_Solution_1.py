
# Space: O(n)
# Time: O(n)

import functools


class Solution:
    def isAlienSorted(self, words, order):
        cache = {}
        for index, char in enumerate(order):
            cache[char] = index

        def custom_sort(a, b):
            index_a, index_b = 0, 0
            while index_a < len(a) and index_b < len(b):
                if cache[a[index_a]] > cache[b[index_b]]:
                    return 1
                elif cache[a[index_a]] < cache[b[index_b]]:
                    return -1
                index_a += 1
                index_b += 1
            if len(a) > len(b):
                return 1
            elif len(a) < len(b):
                return -1
            return 0

        new_list = sorted(words, key=functools.cmp_to_key(custom_sort))

        return new_list == words




