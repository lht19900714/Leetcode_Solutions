
# Space: O(n)
# Time: O(n)


import collections


class Solution:
    def getHint(self, secret, guess):
        data = collections.Counter(secret)
        num_of_A, num_of_B = 0, 0
        non_matched_index = set()

        # check matched char
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                num_of_A += 1
                data[secret[i]] -= 1
            else:
                non_matched_index.add(i)

        # check un-matched char
        for i in non_matched_index:
            if guess[i] in data and data[guess[i]] > 0:
                num_of_B += 1
                data[guess[i]] -= 1

        return f'{num_of_A}A{num_of_B}B'







