
# Space: O(n)
# Time: O(n^2)

class Solution:
    def repeatedSubstringPattern(self, s) -> bool:
        spliter = s[0]

        for i in range(1, len(s)):
            temp_res = s.split(spliter)
            if len(set(temp_res)) == 1 and '' in temp_res:
                return True
            spliter += s[i]

        return False




