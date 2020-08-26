
# Space: O(1)
# Time: O(n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.cache = {}

        def helper(x, n):
            if n == 0: return 1
            if n == 1: return x
            if n in self.cache: return self.cache[n]

            flag_negative = True if n < 0 else False
            flag_odd = True if n % 2 != 0 else False

            if flag_odd:
                res = helper(x, abs(n) // 2) * helper(x, abs(n) // 2) * x
            else:
                res = helper(x, abs(n) // 2) * helper(x, abs(n) // 2)

            if flag_negative:
                self.cache[n] = 1 / res
                return 1 / res

            self.cache[n] = res
            return res

        return helper(x, n)




