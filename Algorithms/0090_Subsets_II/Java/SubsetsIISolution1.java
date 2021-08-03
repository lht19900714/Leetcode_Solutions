
// Space: O(n)
// Time: O(n)

class Solution {
    List<List<Integer>> res = new ArrayList<>();
    boolean[] status = null;
    Set<String> cache = new HashSet<>();

    public List<List<Integer>> subsetsWithDup(int[] nums) {

        if (nums.length == 0) return new ArrayList<>();
        status = new boolean[nums.length];
        Arrays.fill(status, false);
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            generateSubset(nums, i, nums.length, new ArrayList<>());
        }
        return res;
    }

    private void generateSubset(int[] nums, int index, int limit, ArrayList<Integer> temp) {
        if (temp.size() > limit) return;
        if (!cache.contains(temp.toString())) {
            res.add(new ArrayList<>(temp));
            cache.add(temp.toString());
        }

        for (int i = index; i < nums.length; i++) {
            if (!status[i]) {
                temp.add(nums[i]);
                status[i] = true;
                generateSubset(nums, i + 1, limit, temp);
                status[i] = false;
                temp.remove(temp.size() - 1);
            }
        }
    }
}




