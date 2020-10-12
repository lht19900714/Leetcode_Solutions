
# Space: O(n)
# Time: O(n)

import collections

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if (len(A) == 0 and len(B) > 0) or (len(A) > 0 and len(B) == 0) or (len(A) != len(B)): return False

        count = 0
        index = []
        for i in range(len(A)):
            if A[i] != B[i]:
                index.append(i)
                count += 1

        if count == 2:
            return True if A[index[0]] == B[index[1]] and A[index[1]] == B[index[0]] else False

        if count > 2 or count == 1: return False

        if count == 0:
            temp = collections.Counter(A)

            for key in temp:
                if temp[key] > 1: return True

        return False




