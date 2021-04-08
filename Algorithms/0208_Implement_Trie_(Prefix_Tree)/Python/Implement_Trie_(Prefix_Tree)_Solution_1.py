
# Space: O(n)
# Time: O(n)

# Structure explanation
# dictionary = {char + flag : {}}
# char = single character
# flag = indicator of the end of word

# Example:
# word "apple", "app","ape" in the Trie:
# Trie = {'a0':
#             {'p0':
#                  {'p1':
#                       {'l0':
#                            {'e1'{}
#                       },
#                   'e1':{}
#                  }
#              }
#         }
#


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        def _insert(word, index, length, branch):
            if index >= length: return

            current_branch = self._search_char(word[index], branch)

            # if current character exists in Trie
            if current_branch:
                if index == length - 1:
                    if current_branch[-1] == '0':
                        branch[word[index] + '1'] = branch[current_branch]
                        branch.pop(current_branch)
                        return
                else:
                    _insert(word, index + 1, length, branch[current_branch])

            # if current character does NOT exist in Trie
            else:
                new_branch = word[index]
                if index == length - 1:
                    branch[new_branch + '1'] = {}
                    return
                else:
                    branch[new_branch + '0'] = {}
                    _insert(word, index + 1, length, branch[new_branch + '0'])

        word_length = len(word)
        _insert(word, 0, word_length, self.data)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        word_length = len(word)
        return self._search_word(word, 0, word_length, self.data, 1)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        prefix_length = len(prefix)
        return self._search_word(prefix, 0, prefix_length, self.data, 0)

    def _search_word(self, word, index, length, branch, flag):  # use flag to indicate find whole word or prefix
        if len(word) == 0: return False

        current_branch = self._search_char(word[index], branch)

        if current_branch:
            if index == length - 1 and current_branch[-1] == '1':
                return True
            elif index == length - 1 and current_branch[-1] != '1':
                return False if flag == 1 else True
            else:
                return self._search_word(word, index + 1, length, branch[current_branch], flag)
        else:
            return False

    def _search_char(self, target_char, branch):
        for char in branch:
            if char[0] == target_char:
                return char
        return None



