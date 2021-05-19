
// Space: O(n)
// Time: O(n)

class Solution {
    public int longestStrChain(String[] words) {
        if (words.length == 1) return 1;
        int res = 0;
        Map<String, Integer> cache = new HashMap<>();
        List<String> wordList = new ArrayList<>();
        Set<String> wordSet = new HashSet<>();
        Collections.addAll(wordSet, words);
        for (String w : words) {
            res = Math.max(res, dfs(w, wordSet, cache));
        }
        return res;
    }

    private int dfs(String word, Set<String> words, Map<String, Integer> cache) {
        if (word.length() == 0) return 0;
        if (word.length() == 1) {
            cache.put(word, 1);
            return 1;
        }
        if (cache.containsKey(word)) return cache.get(word);
        int res = 1;
        for (int i = 0; i < word.length(); i++) {
            String temp = word.substring(0, i) + word.substring(i + 1);
            if (words.contains(temp)) {
                res = Math.max(res, dfs(temp, words, cache) + 1);
            }
        }
        cache.put(word, res);
        return res;
    }
}




