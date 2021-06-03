
# Space: O(n)
# Time: O(n)

class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]

        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        h_max = max(horizontalCuts[i] - horizontalCuts[i - 1] for i in range(1, len(horizontalCuts)))
        v_max = max(verticalCuts[i] - verticalCuts[i - 1] for i in range(1, len(verticalCuts)))

        return (h_max * v_max) % (pow(10, 9) + 7)





