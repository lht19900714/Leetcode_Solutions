
// Space: O(n)
// Time: O(n)

public class Solution {

    public int longestStrChain(String[] words) {
        if (words.length == 1) return 1;
        int res = 0;
        Arrays.sort(words, (s1, s2) -> {
            return s1.length() - s2.length();
        });
        Map<String, Integer> cache = new HashMap<>();

        for (String word : words) {
            cache.put(word, 1);
            if (word.length() == 1) continue;

            for (int i = 0; i < word.length(); i++) {
                String temp = word.substring(0, i) + word.substring(i + 1);
                if (cache.containsKey(temp)) {
                    cache.put(word, Math.max(cache.get(word), cache.get(temp) + 1));
                    res = Math.max(cache.get(word), res);
                }
            }
        }
        return res;
    }
}




