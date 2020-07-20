
# Space: O(n)
# Time: O(n)

# Solution without collections library

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.key_stack = []
        self.status = 0

    def get(self, key: int) -> int:
        if key in self.storage:
            self._refersh(key)
            return self.storage[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self._refersh(key)
            self.storage[key] = value
        else:
            if self.status < self.capacity:
                self.storage[key] = value
                self.key_stack.insert(0, key)
                self.status += 1
            else:
                delete_key = self.key_stack.pop()
                self.storage.pop(delete_key)
                self.storage[key] = value
                self.key_stack.insert(0, key)

    def _refersh(self, key):
        self.key_stack.remove(key)
        self.key_stack.insert(0, key)

