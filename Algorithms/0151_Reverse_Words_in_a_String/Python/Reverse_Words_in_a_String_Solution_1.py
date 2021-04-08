
# Space: O(n)
# Time: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        temp_list = s.split(' ')[::-1]
        res = ''
        for i in temp_list:
            if i != '':
                res += i.strip()
                res += ' '
        return res[:-1]

