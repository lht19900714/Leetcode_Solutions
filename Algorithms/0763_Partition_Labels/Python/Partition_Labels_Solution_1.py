
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def partitionLabels(self, S):
        length = len(S)
        position = collections.defaultdict(int)
        res = []

        # track all characters biggest index
        for i in range(length):
            position[S[i]] = i

        start_pointer, end_pointer = 0, 0

        while end_pointer < length:
            # make end_pointer point to the last index of current character
            end_pointer = position[S[end_pointer]]

            # check character's last index before end_pointer
            # if all characters' last index less than end_pointer, then we found a result; else move end_pointer one step
            for char in set(S[start_pointer:end_pointer + 1]):
                if position[char] > end_pointer:
                    end_pointer += 1
                    break
            else:
                res.append(end_pointer - start_pointer + 1)
                end_pointer += 1
                start_pointer = end_pointer

        return res





