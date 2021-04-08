
# Space: O(n)
# Time: O(n)
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length1 = len(s1)
        length2 = len(s2)
        if length1 > length2: return False
        if length2 == 0: return False
        slow, fast = 0, 0
        data = collections.Counter(s1)
        match = len(data)
        while fast < length2:
            if s2[fast] in data:
                data[s2[fast]] -= 1
                if data[s2[fast]] == 0:
                    match -= 1
                    while match == 0 and slow <= fast:
                        if len(s2[slow:fast + 1]) == length1:
                            return True
                        if s2[slow] in data:
                            data[s2[slow]] += 1
                            if data[s2[slow]] > 0:
                                match += 1
                        slow += 1
            fast += 1
        return False


