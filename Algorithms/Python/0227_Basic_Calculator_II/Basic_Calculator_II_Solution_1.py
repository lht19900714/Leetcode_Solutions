
# Space: O(n)
# Time: O(n)

import re


class Solution:
    def calculate(self, s):
        if len(s) == 0: return 0
        alist = re.findall(r'\d+|[\+\-\*\/]', s)  # get all numbers and operation signs

        temp_res = []
        sign = None

        # calculate '*' and '/'
        for each in alist:
            if each.isdigit() and sign is None:
                temp_res.append(int(each))
            elif each.isdigit() and sign is not None:
                if sign == '*':
                    temp_res[-1] = temp_res[-1] * int(each)
                elif sign == '/':
                    temp_res[-1] = temp_res[-1] // int(each)
                sign = None
            else:
                if each == '*' or each == '/':
                    sign = each
                else:
                    temp_res.append(each)

        # calculate '+' and '-'
        res = 0
        sign = None
        for each in temp_res:
            if type(each) == int and (sign == '+' or sign is None):
                res += each
                sign = None
            elif type(each) == int and sign == '-':
                res -= each
                sign = None
            else:
                sign = each
        return res







