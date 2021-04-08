
# Space: O(1)
# Time: O(n^2)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length <= 1: return s
        self.res = ''

        for i in range(0, length - 1):
            # find palindrome in "aba" pattern
            temp_res_1 = self.find_Palindrome(s, 0, length - 1, i)

            # find palindrome in "abba" pattern
            temp_res_2 = self.find_Palindrome(s, 0, length - 1, i, i + 1) if i <= length - 2 else ''

            self.res = max(self.res, temp_res_1, temp_res_2, key=lambda x: len(x))

        return self.res

    def find_Palindrome(self, string, left, right, x1, x2=-1):

        if x2 == -1:
            cur_left, cur_right = x1, x1
        else:
            cur_left, cur_right = x1, x2

        while cur_left >= left and cur_right <= right and string[cur_left] == string[cur_right]:
            cur_left -= 1
            cur_right += 1

        return string[cur_left + 1:cur_right]



