
// Space: O(n)
// Time: O(n)

class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> res = new ArrayList<>();
        Map<Character, Character> cache = new HashMap<>();
        for (String word : words) {
            if (word.length() != pattern.length()) continue;
            Map<Character, Character> temp = new HashMap<>();
            boolean flag = true;
            for (int i = 0; i < word.length(); i++) {
                if (temp.containsKey(word.charAt(i)) && temp.get(word.charAt(i)) != pattern.charAt(i)) {
                    flag = false;
                    break;
                }
                if (!temp.containsKey(word.charAt(i))) {
                    cache.put(pattern.charAt(i), word.charAt(i));
                    temp.put(word.charAt(i), pattern.charAt(i));
                }
            }
            if (flag) {
                StringBuilder tempRes = new StringBuilder();
                for (char c : pattern.toCharArray()) {
                    tempRes.append(cache.get(c));
                }
                if (word.equals(tempRes.toString())) res.add(word);
            }
        }
        return res;
    }
}





