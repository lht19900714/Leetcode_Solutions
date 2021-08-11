
// Space: O(n)
// Time: O(n)

class Solution {
    public int minFlipsMonoIncr(String s) {
        if (s.length() == 1) return 0;
        int[] lCache = new int[s.length()];
        int[] rCache = new int[s.length()];
        int res;
        lCache[0] = s.charAt(0) == '0' ? 0 : 1;
        rCache[s.length() - 1] = s.charAt(s.length() - 1) == '1' ? 0 : 1;

        for (int i = 1; i < s.length(); i++) {
            lCache[i] = lCache[i - 1] + s.charAt(i) - '0';
        }

        for (int i = s.length() - 2; i >= 0; i--) {
            rCache[i] = rCache[i + 1] + '1' - s.charAt(i);
        }

        res = Math.min(lCache[s.length() - 1], rCache[0]);

        for (int i = 0; i < s.length() - 1; i++) {
            res = Math.min(res, lCache[i] + rCache[i + 1]);
        }
        // use following loop is also correct
        // for (int i = 1; i < s.length(); i++) {
        //     res = Math.min(res, lCache[i - 1] + rCache[i]);
        // }

        return res;
    }
}





