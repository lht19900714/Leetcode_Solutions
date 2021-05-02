# Space: O(n)
# Time: O(n)

class WordFilter:

    def __init__(self, words):
        self.normal_dict = {w: i for i, w in enumerate(words)}
        self.prefix_dict = {}
        self.suffix_dict = {}

        for word in words:
            self.save_dict_tree(word, self.prefix_dict)
            word = word[::-1]
            self.save_dict_tree(word, self.suffix_dict)

    def f(self, prefix: str, suffix: str) -> int:
        pass
        res = -1
        prefix_word, suffix_word = set(), set()
        prefix_whole_word_flag, prefix_dict = self.search_word(prefix, self.prefix_dict)
        suffix_whole_word_flag, suffix_dict = self.search_word(suffix[::-1], self.suffix_dict)
        if prefix_whole_word_flag:
            prefix_word.add(prefix)
        else:
            prefix_word_candidate = self.build_words(prefix_dict)
            for i in prefix_word_candidate:
                prefix_word.add(prefix + i)

        if suffix_whole_word_flag:
            suffix_word.add(suffix)
        else:
            suffix_word_candidate = self.build_words(suffix_dict)
            for i in suffix_word_candidate:
                suffix_word.add(i[::-1] + suffix)

        for word in prefix_word:
            if word in suffix_word:
                res = self.normal_dict[word] if self.normal_dict[word] > res else res
        return res

    def save_dict_tree(self, word, dict_tree):
        length = len(word)
        index = 0
        cur_dict = dict_tree
        while index < length:
            cur_char = word[index]
            if cur_char not in cur_dict:
                cur_dict[cur_char] = {}
            cur_dict = cur_dict[cur_char]
            index += 1

        if '#' not in cur_dict:
            cur_dict['#'] = {}

    def search_word(self, text, dict_tree):
        length = len(text)
        if length == 0: return dict_tree
        index = 0
        cur_dict = dict_tree
        while index < length:
            cur_char = text[index]
            if cur_char not in cur_dict:
                return False, {}
            elif cur_char in cur_dict:
                cur_dict = cur_dict[cur_char]
                index += 1
        if len(cur_dict) == 1 and '#' in cur_dict:
            return True, cur_dict
        return False, cur_dict

    def build_words(self, dict_tree):
        temp_res_list = []

        def _build_word(dict_tree, temp_res):
            for c in dict_tree:
                if c == '#':
                    temp_res_list.append(temp_res)
                elif c != '#':
                    temp_res += c
                    _build_word(dict_tree[c], temp_res)
                    temp_res = temp_res[:-1]

        _build_word(dict_tree, '')
        return temp_res_list




