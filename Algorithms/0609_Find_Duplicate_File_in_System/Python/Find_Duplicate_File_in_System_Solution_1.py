
# Space: O(n)
# Time: O(n)

import collections
import re


class Solution:
    def findDuplicate(self, paths):
        cache = collections.defaultdict(list)
        regex = re.compile('^(.+)\((.+)\)$')
        for each in paths:
            temp = each.split(' ')
            root_path = temp[0]
            for i in range(1, len(temp)):
                file_name = regex.match(temp[i]).group(1)
                file_content = regex.match(temp[i]).group(2)
                cache[file_content].append(root_path + '/' + file_name)

        return [v for k, v in cache.items() if len(v) > 1]





