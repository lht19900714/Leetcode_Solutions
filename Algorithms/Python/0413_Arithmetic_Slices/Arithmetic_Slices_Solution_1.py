
# Space: O(n)
# Time: O(n)


class Solution:
    def numberOfArithmeticSlices(self, A):
        length = len(A)
        self.res = 0

        def slice(alist, index):
            if index < 2: return 0
            temp_res = 0
            if alist[index] - alist[index - 1] == alist[index - 1] - alist[index - 2]:
                temp_res = slice(alist, index - 1) + 1
                self.res += temp_res
            else:
                slice(alist, index - 1)
            return temp_res

        slice(A, length - 1)
        return self.res






