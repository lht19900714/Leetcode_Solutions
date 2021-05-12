
// Space: O(n)
// Time: O(n)

class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int length = cardPoints.length;
        if (k == length) return Arrays.stream(cardPoints).sum();

        int left = 0, right = length - k;
        int minSum = Arrays.stream(Arrays.copyOfRange(cardPoints, left, right)).sum();
        int curSum = Arrays.stream(Arrays.copyOfRange(cardPoints, left, right)).sum();

        while (right < length) {
            curSum = curSum - cardPoints[left] + cardPoints[right];
            minSum = Math.min(curSum, minSum);
            left++;
            right++;
        }
        return Arrays.stream(cardPoints).sum() - minSum;
    }
}





