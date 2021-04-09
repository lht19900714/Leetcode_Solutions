
# Space: O(n)
# Time: O(n)

class Solution:
    def isAlienSorted(self, words, order):
        cache = {}
        for index, char in enumerate(order):
            cache[char] = index

        return words == sorted(words, key=lambda x: [cache[char] for char in x])




