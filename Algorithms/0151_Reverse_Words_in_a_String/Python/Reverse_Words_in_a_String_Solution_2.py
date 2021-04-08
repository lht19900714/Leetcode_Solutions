
# Space: O(n)
# Time: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        temp_list = s.split(' ')
        res = []
        for i in temp_list:
            if i != '':
                res.insert(0, i.strip())
        return ' '.join(res)

