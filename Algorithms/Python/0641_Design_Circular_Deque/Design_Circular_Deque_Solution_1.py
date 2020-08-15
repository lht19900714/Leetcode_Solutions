
# Space: O(n)
# Time: O(n)

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.data = [None] * k
        self.status = 0
        self.size = len(self.data)
        self.head = 0
        self.last = self.head

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            if self.data[self.head] is None:
                self.data[self.head] = value
            else:
                self.head = (self.head - 1) % self.size
                self.data[self.head] = value
            self.status += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            if self.data[self.last] is None:
                self.data[self.last] = value
            else:
                self.last = (self.last + 1) % self.size
                self.data[self.last] = value
            self.status += 1
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.data[self.head] = None
            self.status -= 1
            if self.status != 0:
                self.head = (self.head + 1) % self.size
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.data[self.last] = None
            self.status -= 1
            if self.status != 0:
                self.last = (self.last - 1) % self.size
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.data[self.head] if not self.isEmpty() else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.data[self.last] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.status == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.status == self.size



