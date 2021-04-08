
# Space: O(n)
# Time: O(n)

# Using Trie structure

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """

        def _insert(word, index, length, branch):
            if index >= length: return
            current_branch = self._search_char(word[index], branch)
            if current_branch:
                if index == length - 1:
                    if current_branch[-1] == 0:
                        branch[word[index] + '1'] = branch[current_branch]
                        branch.pop(current_branch)
                        return
                else:
                    _insert(word, index + 1, length, branch[current_branch])
            else:
                new_branch = word[index]
                if index == length - 1:
                    branch[new_branch + '1'] = {}
                    return
                else:
                    branch[new_branch + '0'] = {}
                    _insert(word, index + 1, length, branch[new_branch + '0'])

        word_length = len(word)
        _insert(word, 0, word_length, self.trie)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def _search(word, index, length, branch):
            if len(word) <= 0: return False
            if index >= length: return False

            # handle "." situation
            if word[index] == '.':
                for char in branch:
                    if index == length - 1 and char[-1] == '1': return True
                    if _search(word, index + 1, length, branch[char]):
                        return True
                return False

            current_branch = self._search_char(word[index], branch)
            if current_branch:
                if index == length - 1 and current_branch[-1] == '1':
                    return True
                elif index == length - 1 and current_branch[-1] == '0':
                    return False
                else:
                    return _search(word, index + 1, length, branch[current_branch])
            else:
                return False

        word_length = len(word)
        return _search(word, 0, word_length, self.trie)

    def _search_char(self, target_char, branch):
        for char in branch:
            if char[0] == target_char:
                return char
        return None




