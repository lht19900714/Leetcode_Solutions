
// Space: O(n)
// Time: O(n)

class NumArray {
    private int[] cache = null;
    private int sum = 0;

    public NumArray(int[] nums) {
        cache = nums;
        sum = Arrays.stream(nums).sum();
    }

    public void update(int index, int val) {
        sum -= cache[index];
        sum += val;
        cache[index] = val;
    }

    public int sumRange(int left, int right) {
        int res = sum;
        int index = 0;
        while (index != left) {
            res -= cache[index];
            index++;
        }
        index = cache.length - 1;
        while (index != right) {
            res -= cache[index];
            index--;
        }
        return res;
    }
}





