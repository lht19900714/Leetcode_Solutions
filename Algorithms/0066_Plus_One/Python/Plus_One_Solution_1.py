
# Space: O(n)
# Time: O(n)


class Solution:
    def plusOne(self, digits):
        temp = ''.join(map(lambda x: str(x), digits))
        temp = int(temp) + 1
        temp = list(str(temp))
        return list(map(lambda x: int(x), temp))




