
# Space: O(n)
# Time: O(n)

import re

class Solution:
    def isNumber(self, s: str) -> bool:
        if s[0].isalpha(): return False

        integer_pattern = re.compile("^[+-]?\d+$")
        decimal_pattern = re.compile("(^[+-]?\d+\.\d*$)|(^[+-]?\.\d+$)")

        if s.count('e') == 1 and s.count('E') == 0:
            left = s[:s.index('e')]
            right = s[s.index('e') + 1:]
            if re.match(integer_pattern, left) or re.match(decimal_pattern, left):
                if re.match(integer_pattern, right):
                    return True
            return False

        if s.count('e') == 0 and s.count('E') == 1:
            left = s[:s.index('E')]
            right = s[s.index('E') + 1:]
            if re.match(integer_pattern, left) or re.match(decimal_pattern, left):
                if re.match(integer_pattern, right):
                    return True
            return False

        if s.count('e') == 0 and s.count('E') == 0:
            if re.match(integer_pattern, s) or re.match(decimal_pattern, s):
                return True
            return False

        return False





