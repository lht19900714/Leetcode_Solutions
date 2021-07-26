

// Space: O(1)
// Time: O(n)

public class Solution {
    private int[] original;

    public Solution(int[] nums) {
        original = nums;
    }

    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return original;
    }

    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        int[] res = new int[original.length];
        List<Integer> cache = new ArrayList<>();
        Random rand = new Random();
        for (int i : original) {
            cache.add(i);
        }
        for (int i = 0; i < original.length; i++) {
            int tempIndex = rand.nextInt(cache.size());
            res[i] = cache.get(tempIndex);
            cache.remove(tempIndex);
        }
        return res;
    }
}




