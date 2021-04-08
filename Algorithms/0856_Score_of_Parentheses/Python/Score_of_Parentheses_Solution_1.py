
# Space: O(n)
# Time: O(n^2)

class Solution:
    def scoreOfParentheses(self, S):
        if len(S) == 2: return 1
        cache = list(S)

        while len(cache) != 1:
            index = 1
            while index < len(cache):
                if cache[index - 1] == '(' and cache[index] == ')':
                    cache = cache[:index - 1] + [1] + cache[index + 1:]
                elif isinstance(cache[index - 1], int) and isinstance(cache[index], int):
                    temp_score = cache[index - 1] + cache[index]
                    cache = cache[:index - 1] + [temp_score] + cache[index + 1:]
                elif index < len(cache) - 1 and cache[index - 1] == '(' and isinstance(cache[index], int) and cache[index + 1] == ')':
                    temp_score = cache[index] * 2
                    cache = cache[:index - 1] + [temp_score] + cache[index + 2:]
                else:
                    index += 1

        return cache[0]





