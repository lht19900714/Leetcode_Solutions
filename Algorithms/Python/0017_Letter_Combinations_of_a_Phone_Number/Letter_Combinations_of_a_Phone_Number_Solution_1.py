# Space: O(n)
# Time: O(n)

# BFS approach

import collections


class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        # build dictionary to map digits to characters
        data = collections.defaultdict(list)
        pointer = 97  # chr(97) =='a'    chr(65) == 'A'
        for i in range(1, 10):
            count = 3  # default each digit has 3 characters
            if i == 1:
                data[str(i)] = ''
                continue
            if i == 7 or i == 9:
                count = 4
            while count:
                data[str(i)].append(chr(pointer))
                pointer += 1
                count -= 1

        # loop through each number from input in push it into queue,
        # then continuously update each item in the queue
        queue = []

        for char in digits:
            count = len(queue)
            if count == 0:
                queue = data[char][:]
                continue
            else:
                while count:
                    cur = queue.pop(0)
                    for i in data[char]:
                        queue.append(cur + i)
                    count -= 1

        return queue



