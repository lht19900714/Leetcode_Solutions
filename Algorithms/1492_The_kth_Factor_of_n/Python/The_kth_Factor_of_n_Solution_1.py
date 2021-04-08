

# Space: O(1)
# Time: O(n)

class Solution:
    def kthFactor(self, n, k):
        if k == 1: return 1

        counter = 0
        for i in range(1, n + 1):
            if n % i == 0:
                counter += 1
                if counter == k: return i

        return -1






