
# Space: O(n)
# Time: O(n)


import collections


class MapSum:

    def __init__(self):
        self.number_dict = {}
        self.prefix_dict = collections.defaultdict(list)

    def insert(self, key: str, val: int) -> None:
        if key not in self.number_dict:
            for i in range(1, len(key) + 1):
                self.prefix_dict[key[:i]].append(key)
        self.number_dict[key] = val

    def sum(self, prefix: str) -> int:
        return sum(self.number_dict[key] for key in self.prefix_dict[prefix])





