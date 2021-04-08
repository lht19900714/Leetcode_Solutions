
# Space: O(1)
# Time: O(n)

class Solution:
    def bagOfTokensScore(self, tokens, P):
        length = len(tokens)
        if length == 1:
            return 0 if tokens[0] > P else 1

        tokens.sort()

        res, score = 0, 0

        while tokens:
            if tokens[0] <= P:
                score += 1
                res = max(score, res)
                P -= tokens[0]
                tokens.pop(0)
            elif score > 0:
                score -= 1
                P += tokens[-1]
                tokens.pop()
            else:
                break

        return res




