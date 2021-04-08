
# Space: O(n)
# Time: O(n^2)

class Solution:
    def partition(self, s):
        length = len(s)
        if length == 1: return [[s]]
        self.res = []

        def backtracking(string, start_index, temp_res):
            if start_index == len(string):
                self.res.append(temp_res[:])
                return

            for i in range(start_index + 1, len(string) + 1):
                if self.check_palindrome(string[start_index:i]):
                    temp_res.append(string[start_index:i])
                    backtracking(string, i, temp_res)
                    temp_res.pop()

        backtracking(s, 0, [])
        return self.res

    def check_palindrome(self, string):
        length = len(string)
        if length % 2 == 0:
            left, right = length // 2 - 1, length // 2
        else:
            left, right = length // 2, length // 2

        while left >= 0 and right < length:
            if string[left] == string[right]:
                left -= 1
                right += 1
            else:
                return False
        return True




