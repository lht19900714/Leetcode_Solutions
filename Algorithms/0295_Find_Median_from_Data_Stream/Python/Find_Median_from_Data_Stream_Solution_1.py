
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.count == 0:
            self.data.append(num)
            self.count += 1
            return

        # find the desired position for input number
        position = self.binary_search(self.data, num)

        if position == -1:
            self.data.append(num)
        else:
            self.data.insert(position, num)

        self.count += 1

    def findMedian(self) -> float:

        # 2 situation: odd median / even median
        if self.count / 2 == self.count // 2:
            ans = (self.data[self.count // 2] + self.data[self.count // 2 - 1]) / 2
            return ans
        else:
            return self.data[self.count // 2]


    def binary_search(self, alist, target):
        length = len(alist)
        left, right = 0, length - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if alist[mid] < target:
                left = mid + 1
            else:
                right = mid

        if alist[left] >= target:
            return left
        if alist[right] >= target:
            return right
        else:
            return -1







