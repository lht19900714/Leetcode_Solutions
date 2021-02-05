
# Space: O(n)
# Time: O(n)

import re


class Solution:
    def simplifyPath(self, path):
        multiple_slash_pattern = re.compile(r'/+')

        path = multiple_slash_pattern.sub('/', path)
        path = path.strip('/')
        path_list = path.split('/')
        res = []

        for item in path_list:
            if item == '..':
                if res:
                    res.pop()
            elif item == '.':
                continue
            else:
                res.append(item)

        return '/' + '/'.join(res)




