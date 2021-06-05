
// Space: O(n)
// Time: O(n)

class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> cache = new HashSet<>();
        for (String s : deadends) cache.add(s);
        if (cache.contains(target) || cache.contains("0000")) return -1;
        int step = 0;
        Queue<String> queue = new ArrayDeque<>();
        queue.add("0000");

        while (!queue.isEmpty()) {
            int count = queue.size();
            while (count-- > 0) {
                String cur = queue.poll();
                if (cur.equals(target)) return step;
                for (int i = 0; i < cur.length(); i++) {
                    int tempNum = Character.getNumericValue((int) cur.charAt(i));
                    StringBuilder t1, t2;
                    t1 = new StringBuilder(cur.substring(0, i)).append(String.valueOf((10 + tempNum + 1) % 10)).append(cur.substring(i + 1));
                    t2 = new StringBuilder(cur.substring(0, i)).append(String.valueOf((10 + tempNum - 1) % 10)).append(cur.substring(i + 1));
                    if (!cache.contains(t1.toString())) {
                        queue.add(t1.toString());
                        cache.add(t1.toString());
                    }
                    if (!cache.contains(t2.toString())) {
                        queue.add(t2.toString());
                        cache.add(t2.toString());
                    }
                }
            }
            step++;
        }
        return -1;
    }
}




