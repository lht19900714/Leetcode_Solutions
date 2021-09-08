
# Space: O(1)
# Time: O(n)


class Solution:
    def shiftingLetters(self, s, shifts):
        total = sum(shifts) % 26
        res = []
        for i, c in enumerate(s):
            index = ord(c) - ord('a')
            res.append(chr(ord('a') + (index + total) % 26))
            total = (total - shifts[i]) % 26

        return ''.join(res)




