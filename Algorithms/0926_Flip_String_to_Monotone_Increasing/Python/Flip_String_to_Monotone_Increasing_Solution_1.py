
# Space: O(n)
# Time: O(n)

class Solution:
    def minFlipsMonoIncr(self, s):
        length = len(s)
        if length <= 1: return 0
        res = 0
        cache = list(map(lambda x: int(x), list(s)))
        l_cache = [0 for _ in range(length)]
        r_cache = [0 for _ in range(length)]

        l_cache[0] = cache[0]
        r_cache[-1] = 1 if cache[-1] == 0 else 0

        for i in range(1, length):
            l_cache[i] = cache[i] + l_cache[i - 1]

        for i in range(length - 2, -1, -1):
            if cache[i] == 1:
                r_cache[i] = r_cache[i + 1]
            else:
                r_cache[i] = r_cache[i + 1] + 1

        res = min(l_cache[-1], r_cache[0])

        for i in range(0, length - 1):
            res = min(res, l_cache[i] + r_cache[i + 1])

        # use following loop is also correct
        # for i in range(1, length):
        #     res = min(res, l_cache[i - 1] + r_cache[i])

        return res




