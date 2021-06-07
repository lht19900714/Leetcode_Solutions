
// Space: O(n)
// Time: O(n)

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length <= 1) return nums.length;
        List<Integer> cache = new ArrayList(Arrays.asList(nums));

        int[] cache1 = cache.stream().distinct().sorted().mapToInt(Integer::intValue).toArray();

        int res = 0, counter = 1, index = 1;

        while (index < nums.length) {
            if (nums[index] == nums[index - 1] + 1) {
                counter += 1;
            }
            else {
                res = Math.max(res,counter);
                counter = 1;
            }
            index+=1;
        }
        return Math.max(res,counter);
    }
}




