
# Space: O(n)
# Time: O(n)

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.length = k
        self.first = 0
        self.last = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.queue[self.last] is not None:
                self.last = (self.last + 1) % self.length
            self.queue[self.last] = value
            self.count += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.queue[self.first] = None
        self.count -= 1

        if not self.isEmpty():
            self.first = (self.first + 1) % self.length

        return True

    def Front(self) -> int:

        return -1 if self.isEmpty() else self.queue[self.first]

    def Rear(self) -> int:

        if self.count == 1: return self.queue[self.first]

        return -1 if self.isEmpty() else self.queue[self.last]

    def isEmpty(self) -> bool:

        return True if self.count == 0 else False

    def isFull(self) -> bool:

        return True if self.count == self.length else False



