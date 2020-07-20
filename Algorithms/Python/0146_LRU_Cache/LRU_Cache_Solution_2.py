
# Space: O(n)
# Time: O(n)

# Solution with collections library

import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.length = capacity
        self.data = collections.OrderedDict()
        self.status = 0

    def get(self, key: int) -> int:

        ans = self.data.get(key, None)
        if ans is not None:
            self.data.move_to_end(key)
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data[key] = value
            self.data.move_to_end(key)
        elif self.status < self.length:
            self.data[key] = value
            self.status += 1
        else:
            self.data.popitem(False)
            self.data[key] = value


