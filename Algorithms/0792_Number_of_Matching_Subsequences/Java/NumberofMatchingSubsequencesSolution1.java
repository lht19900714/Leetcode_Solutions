
// Space: O(n)
// Time: O(n)

class Solution {
    private Map<String, Integer> result = new HashMap<>();

    public int numMatchingSubseq(String s, String[] words) {
        int res = 0;
        for (String word : words) {
            if (result.containsKey(word)) res += result.get(word);
            else {
                if (isSubsequence(word, s)) {
                    res += 1;
                    result.put(word, 1);
                } else {
                    result.put(word, 0);
                }
            }
        }
        return res;
    }

    private boolean isSubsequence(String s, String target) {
        int index1 = 0, index2 = 0;
        while (index1 < s.length() && index2 < target.length()) {
            if (s.charAt(index1) == target.charAt(index2)) index1++;
            if (index1 == s.length()) return true;
            index2++;
        }
        return index1 == s.length();
    }
}




