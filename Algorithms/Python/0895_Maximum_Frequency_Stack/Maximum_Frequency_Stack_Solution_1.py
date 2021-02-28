
# Space: O(n)
# Time: O(1)

import collections


class FreqStack:

    def __init__(self):
        self.counter = collections.defaultdict(int)
        self.freq = collections.defaultdict(list)
        self.max_count = 0

    def push(self, x: int) -> None:
        self.counter[x] += 1
        self.freq[self.counter[x]].append(x)
        self.max_count = max(self.max_count, self.counter[x])

    def pop(self) -> int:
        res = self.freq[self.max_count].pop()
        self.counter[res] -= 1
        if not self.freq[self.max_count]:
            self.max_count -= 1
        return res




