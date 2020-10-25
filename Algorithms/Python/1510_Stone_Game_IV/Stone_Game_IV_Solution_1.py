
# Space: O(n)
# Time: O(n)


class Solution:
    def winnerSquareGame(self, n):
        self.data = {}

        def helper(n):
            if n < 1: return False
            if n in self.data: return self.data[n]

            possible_pick = int(pow(n, 0.5))

            for i in range(1, possible_pick + 1):
                if not helper(n - i * i):
                    self.data[n] = True
                    return True

            self.data[n] = False
            return False

        return helper(n)




