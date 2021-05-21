
// Space: O(n)
// Time: O(n)

class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> res = new ArrayList<>();
        for (String word : words) {
            if (word.length() == pattern.length() && verify(word, pattern)) res.add(word);
        }
        return res;
    }

    private boolean verify(String word, String pattern) {
        Map<Character, Character> wordMatch = new HashMap<>();
        Map<Character, Character> patternMatch = new HashMap<>();
        for (int i = 0; i < word.length(); i++) {
            if (!wordMatch.containsKey(word.charAt(i))) wordMatch.put(word.charAt(i), pattern.charAt(i));
            if (!patternMatch.containsKey(pattern.charAt(i))) patternMatch.put(pattern.charAt(i), word.charAt(i));
            if (wordMatch.get(word.charAt(i)) != pattern.charAt(i) || patternMatch.get(pattern.charAt(i)) != word.charAt(i))
                return false;
        }
        return true;
    }
}





