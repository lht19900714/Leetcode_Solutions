
# Space: O(1)
# Time: O(n)

import re

class Solution:
    def ambiguousCoordinates(self, s):
        data = s[1: -1]
        res = []

        for i in range(1, len(data)):
            left_res = self.generate_numbers(data[:i])
            right_res = self.generate_numbers(data[i:])

            if len(left_res) == 0 or len(right_res) == 0: continue

            for i in left_res:
                for j in right_res:
                    temp = '(' + i + ', ' + j + ')'
                    res.append(temp)

        return res

    def generate_numbers(self, string):
        regex_test = re.compile('(^[1-9]+[0-9]*\.[0-9]*[1-9]$)|(^0\.[0-9]*[1-9]$)')
        if len(string) == 1: return [string]
        res = []
        if string.lstrip('0') == string: res.append(string)

        for i in range(1, len(string)):
            temp = string[:i] + '.' + string[i:]
            if regex_test.match(temp): res.append(temp)

        return res





