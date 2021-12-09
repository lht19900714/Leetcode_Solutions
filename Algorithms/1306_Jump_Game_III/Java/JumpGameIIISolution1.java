
// Space: O(n)
// Time: O(n)

class Solution {
    public boolean canReach(int[] arr, int start) {
        if (arr.length == 1) {
            return arr[0] == 0;
        }
        HashSet<Integer> cache = new HashSet<>();
        cache.add(start);
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            if (arr[cur] == 0) return true;
            int left = cur - arr[cur];
            int right = cur + arr[cur];

            if (0 <= left && left < arr.length && !cache.contains(left)) {
                queue.add(left);
                cache.add(left);
            }
            if (0 <= right && right < arr.length && !cache.contains(right)) {
                queue.add(right);
                cache.add(right);
            }
        }
        return false;
    }
}




