
# Space: O(n)
# Time: O(n)

import re
import collections


class Solution:
    def spellchecker(self, wordlist, queries):
        cache = set(wordlist)
        pattern_dict = collections.defaultdict(list)
        res = []

        for word in wordlist:
            key = re.sub('[aeiou]', '*', word, flags=re.IGNORECASE).lower()
            pattern_dict[key].append(word)

        for word in queries:
            # perfect match situation
            if word in cache:
                res.append(word)
                continue

            # pattern match situation
            temp_key = re.sub('[aeiou]', '*', word, flags=re.IGNORECASE).lower()

            if temp_key in pattern_dict:
                temp_res_list = pattern_dict[temp_key]
                temp_res = ''
                for temp_word in temp_res_list:
                    if word.lower() == temp_word.lower():
                        temp_res = temp_word
                        break
                res.append(temp_res if temp_res != '' else temp_res_list[0])
            else:
                res.append('')

        return res




