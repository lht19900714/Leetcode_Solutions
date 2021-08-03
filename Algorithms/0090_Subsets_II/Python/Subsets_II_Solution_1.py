
# Space: O(n)
# Time: O(n)

class Solution:
    def subsetsWithDup(self, nums):
        length = len(nums)
        if length == 0: return [[]]
        if length == 1: return [[], nums]
        nums = sorted(nums)
        self.res = []
        self.status = [False for _ in range(length)]
        for i in range(length):
            self.generate_subset(nums, length, [], i)
        return self.res

    def generate_subset(self, alist, limit, temp, start_index):
        if limit < len(temp): return
        if temp not in self.res: self.res.append(temp[:])

        for i in range(start_index, len(alist)):
            if not self.status[i]:
                temp.append(alist[i])
                self.status[i] = True
                self.generate_subset(alist, limit, temp, i + 1)
                self.status[i] = False
                temp.pop()




