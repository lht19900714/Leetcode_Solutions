
# Space: O(n)
# Time: O(n)


class RecentCounter:

    def __init__(self):
        self.data = []
        self.count = 0

    def ping(self, t: int) -> int:
        self.data.append(t)
        self.count += 1

        while self.data[0] < max(0, t - 3000):
            self.data.pop(0)
            self.count -= 1

        return self.count
