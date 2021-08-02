
// Space: O(1)
// Time: O(n)


class Solution {
    public int trap(int[] height) {
        if (height.length <= 1) return 0;
        int highestBarIndex = 0;
        for (int i = 0; i < height.length; i++) {
            highestBarIndex = height[highestBarIndex] < height[i] ? i : highestBarIndex;
        }
        int res = 0;
        int index = 0;
        int highestBar = 0;
        while (index != highestBarIndex) {
            highestBar = Math.max(highestBar, height[index]);
            res += highestBar - height[index];
            index++;
        }

        index = height.length - 1;
        highestBar = 0;
        while (index != highestBarIndex) {
            highestBar = Math.max(highestBar, height[index]);
            res += highestBar - height[index];
            index--;
        }
        return res;
    }
}




