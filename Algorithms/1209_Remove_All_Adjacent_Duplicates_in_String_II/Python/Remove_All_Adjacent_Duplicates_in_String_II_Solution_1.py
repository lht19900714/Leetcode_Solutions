
# Space: O(1)
# Time: O(n)

class Solution:
    def removeDuplicates(self, s, k):
        length = len(s)
        if length <= 1: return s
        if k > length: return s

        flag = True
        cache = set(list(s))

        while flag:
            for char in cache:
                if char * k in s:
                    s = s.replace(char * k, '')
                    break
            else:
                flag = False

        return s




