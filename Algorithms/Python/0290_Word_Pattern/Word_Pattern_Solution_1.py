
# Space: O(n)
# Time: O(n)

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern and str: return False
        if pattern and not str: return False
        if pattern == str and len(pattern) == 1: return True
        if pattern == str: return False

        # save pattern_char and index pair
        data = {}
        str_list = str.split()

        if len(str_list) != len(pattern): return False

        # loop through pattern, word, and index simultaneously
        for pattern_char, word, index in zip(pattern, str_list, range(len(str_list))):
            # if we have seen this pattern_char, and the current word is not equal to the word at previously saved parrern_char index.
            # then it's not match
            if pattern_char in data and str_list[data[pattern_char]] != word: return False

            # continuely update the seen pattern_char index
            data[pattern_char] = index

        # Handle edge case: if all words in the str are the same.
        return True if len(data) == len(set(str_list)) else False







