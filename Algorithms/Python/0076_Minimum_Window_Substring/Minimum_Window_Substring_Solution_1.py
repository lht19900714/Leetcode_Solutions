
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        t_count = collections.Counter(t)
        total_match_count = len(t_count)
        fast_pointer, slow_pointer = 0, 0
        res = s + t  # initial a impossible result, will be used to compare length during the loop
        while fast_pointer < len(s):
            current_character = s[fast_pointer]
            if current_character in t_count:
                t_count[current_character] -= 1
                if t_count[current_character] == 0:
                    total_match_count -= 1
                    while total_match_count == 0:
                        res = s[slow_pointer:fast_pointer + 1] if len(s[slow_pointer:fast_pointer + 1]) < len(res) else res
                        if s[slow_pointer] in t_count:
                            t_count[s[slow_pointer]] += 1
                            if t_count[s[slow_pointer]] > 0:
                                total_match_count += 1
                        slow_pointer += 1
            fast_pointer += 1
        return res if res != s + t else ''


