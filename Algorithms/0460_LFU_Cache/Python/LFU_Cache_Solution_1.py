
# Space: O(n)
# Time: O(n)

import collections


class LFUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.length = 0
        self.data = {}
        self.frequent_data = collections.OrderedDict()

    def get(self, key: int) -> int:
        res = self.data.get(key, None)
        if res is None: return -1

        self.frequent_data[key] += 1
        self.frequent_data.move_to_end(key)
        return res

    def put(self, key: int, value: int) -> None:

        if self.length < self.size and key not in self.data:
            self.data[key] = value
            self.frequent_data[key] = 1
            self.length += 1

        elif self.length < self.size and key in self.data:
            self.data[key] = value
            self.frequent_data[key] += 1

        elif self.length >= self.size > 0 and key in self.data:
            self.data[key] = value
            self.frequent_data[key] += 1
            self.frequent_data.move_to_end(key)

        elif self.length >= self.size > 0 and key not in self.data:
            delete_key = self.find_delete_target()
            self.data.pop(delete_key)
            self.frequent_data.pop(delete_key)
            self.data[key] = value
            self.frequent_data[key] = 1

    def find_delete_target(self):
        frequency, target_key = None, None

        for key, value in reversed(self.frequent_data.items()):
            if frequency is None or frequency >= value:
                target_key, frequency = key, value

        return target_key




