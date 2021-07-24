
// Space: O(1)
// Time: O(n)

class Solution {
        public String pushDominoes(String dominoes) {
        int[] cache = new int[dominoes.length()];
        int force = 0;

        for (int i = 0; i < dominoes.length(); i++) {
            if (dominoes.charAt(i) == 'R') force = cache.length;
            else if (dominoes.charAt(i) == 'L') force = 0;
            else force = Math.max(force - 1, 0);
            cache[i] += force;
        }

        force = 0;
        for (int i = dominoes.length() - 1; i >= 0; i--) {
            if (dominoes.charAt(i) == 'L') force = cache.length;
            else if (dominoes.charAt(i) == 'R') force = 0;
            else force = Math.max(force - 1, 0);
            cache[i] -= force;
        }

        StringBuilder res = new StringBuilder();
        for (int i : cache) {
            if (i > 0) res.append("R");
            else if (i < 0) res.append("L");
            else res.append(".");
        }
        return res.toString();
        }
}




