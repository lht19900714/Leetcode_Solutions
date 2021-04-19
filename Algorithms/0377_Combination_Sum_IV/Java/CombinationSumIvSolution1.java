
// Space: O(n)
// Time: O(n^2)

public class Solution {
    public Map<Integer, Integer> cache = new HashMap<>();

    public int combinationSum4(int[] nums, int target) {
        dfs(nums, target);
        return cache.get(target);
    }

    private int dfs(int[] nums, int target) {
        if (target < 0) return 0;
        if (target == 0) return 1;
        if (cache.containsKey(target)) return cache.get(target);

        int count = 0;
        for (int num : nums) {
            int tempTarget = target - num;
            count += dfs(nums, tempTarget);
        }
        cache.put(target, count);
        return count;
    }
}




