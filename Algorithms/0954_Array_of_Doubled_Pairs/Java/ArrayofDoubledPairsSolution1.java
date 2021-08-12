
// Space: O(n)
// Time: O(n^2)

class Solution {
    private Map<Integer, Integer> cache = null;
    public boolean canReorderDoubled(int[] arr) {
            if (arr.length == 2) {
            if (arr[0] * 2 == arr[1] || arr[1] * 2 == arr[0]) return true;
            return false;
        }
        cache = new HashMap<>();
        for (int i : arr) {
            cache.put(i, cache.getOrDefault(i, 0) + 1);
        }

        Integer[] temp = new Integer[arr.length];
        for (int i = 0; i < arr.length; ++i)
            temp[i] = arr[i];
        Arrays.sort(temp, Comparator.comparingInt(Math::abs));


        for (Integer i : temp) {
            if (cache.get(i) == 0) continue;
            if (cache.getOrDefault(2 * i, 0) == 0) return false;
            cache.put(i, cache.get(i) - 1);
            cache.put(i * 2, cache.get(i * 2) - 1);
        }
        return true;
    }
}




