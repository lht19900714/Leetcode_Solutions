
# Space: O(n)
# Time: O(n)

# DFS approach

import collections


class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        # build dictionary to map digits to characters
        data = collections.defaultdict(str)
        pointer = 97  # chr(97) =='a'    chr(65) == 'A'
        for i in range(1, 10):
            count = 3  # default each digit has 3 characters
            if i == 1:
                data[str(i)] = ''
                continue
            if i == 7 or i == 9:
                count = 4
            while count:
                data[str(i)] += chr(pointer)
                pointer += 1
                count -= 1

        def dfs(digits, index, temp_res, res):
            if len(digits) == index:
                res.append(temp_res)
                return
            for char in data[digits[index]]:
                temp_res += char
                dfs(digits, index + 1, temp_res, res)
                temp_res = temp_res[:-1]
            return res

        return dfs(digits,0,'',[])




