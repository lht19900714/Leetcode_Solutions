
# Space: O(n)
# Time: O(n)

class NumArray:

    def __init__(self, nums):
        self.sum = sum(nums)
        self.cache = nums
        self.length = len(nums)

    def update(self, index, val):
        self.sum -= self.cache[index]
        self.sum += val
        self.cache[index] = val

    def sumRange(self, left, right):
        res = self.sum
        if left != 0:
            index = 0
            while index != left:
                res -= self.cache[index]
                index += 1
        if right != self.length - 1:
            index = self.length - 1
            while index != right:
                res -= self.cache[index]
                index -= 1
        return res




