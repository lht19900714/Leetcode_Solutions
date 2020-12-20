
# Space: O(1)
# Time: O(n)

class Solution:
    def decodeAtIndex(self, S, K):
        size = 0
        for i in range(len(S)):
            if S[i].isdigit(): size *= int(S[i])
            elif S[i].isalpha(): size += 1

        for i in range(len(S) - 1, -1, -1):
            K = K % size

            if K == 0 and S[i].isalpha(): return S[i]

            if S[i].isalpha(): size -= 1
            elif S[i].isdigit(): size /= int(S[i])





