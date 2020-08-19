
# Space: O(n)
# Time: O(n)

import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = set()
        self.list = []
        self.length = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val not in self.data:
            self.data.add(val)
            self.list.append(val)
            self.length += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            self.data.remove(val)
            self.list.remove(val)
            self.length -= 1
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        random_number = random.randint(0, self.length - 1)
        return self.list[random_number]





