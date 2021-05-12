
# Space: O(n)
# Time: O(n)

class Solution:
    def maxScore(self, cardPoints, k):

        length = len(cardPoints)
        if length == k: return sum(cardPoints)

        left, right = 0, length - k
        min_sum = cur_sum = sum(cardPoints[left:right])

        while right < length:
            cur_sum = cur_sum - cardPoints[left] + cardPoints[right]
            min_sum = min(min_sum, cur_sum)
            left += 1
            right += 1

        return sum(cardPoints) - min_sum





