
// Space: O(n)
// Time: O(n)

class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        Arrays.sort(horizontalCuts);
        Arrays.sort(verticalCuts);

        int hMax = horizontalCuts[0], vMax = verticalCuts[0];

        for (int i = 1; i < horizontalCuts.length; i++) {
            hMax = Math.max(hMax, horizontalCuts[i] - horizontalCuts[i - 1]);
        }
        hMax = Math.max(hMax, h - horizontalCuts[horizontalCuts.length - 1]);

        for (int i = 1; i < verticalCuts.length; i++) {
            vMax = Math.max(vMax, verticalCuts[i] - verticalCuts[i - 1]);
        }
        vMax = Math.max(vMax, w - verticalCuts[verticalCuts.length - 1]);

        return (int) (vMax * 1L * hMax % (Math.pow(10, 9) + 7));
    }
}





