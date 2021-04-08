# Space: O(n)
# Time: O(n)


class Solution:
    def numPairsDivisibleBy60(self, time):
        res = 0
        cache = [0 for _ in range(60)]

        # count each number of modulo 60, and store that in an array of size 60.
        for i in time:
            index = i % 60
            cache[index] += 1

        i, j = 1, 59

        while i < j:
            res += cache[i] * cache[j]
            i += 1
            j -= 1

        # special scenarios,
        # if modulo 60 is 0 or modulo 60 is 30, they can pair each other.
        res += sum((z for z in range(1, cache[i])))
        res += sum((z for z in range(1, cache[0])))

        return res
