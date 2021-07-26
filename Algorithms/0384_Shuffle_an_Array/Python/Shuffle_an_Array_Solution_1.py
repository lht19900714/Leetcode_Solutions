
# Space: O(n)
# Time: O(n)

import random


class Solution:

    def __init__(self, nums):
        self.original = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        res = []
        temp = self.original[:]
        while temp:
            temp_num = random.choice(temp)
            res.append(temp_num)
            temp.remove(temp_num)
        return res




