
// Space: O(n)
// Time: O(n)

class Solution {
    public boolean checkPossibility(int[] nums) {
        int length = nums.length;
        if (length <= 1) return true;
        List<List<Integer>> cache = new ArrayList<>();
        int index = 0, count = 0;

        while (index < length) {
            boolean startFlag = true;
            List<Integer> temp = new ArrayList<>();
            while (index < length && (startFlag || nums[index - 1] <= nums[index])) {
                temp.add(nums[index]);
                index++;
                startFlag = false;
            }
            cache.add(temp);
            count++;
            if (count > 2) return false;
        }
        if (count < 2) return true;
        if (cache.get(0).size() == 1 || cache.get(1).size() == 1) return true;
        if (cache.get(0).get(cache.get(0).size() - 2) <= cache.get(1).get(0)) return true;
        if (cache.get(0).get(cache.get(0).size() - 1) <= cache.get(1).get(1)) return true;
        return false;
    }
}




