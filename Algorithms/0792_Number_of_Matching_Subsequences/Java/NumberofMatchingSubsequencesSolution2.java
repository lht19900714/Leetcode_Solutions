
// Space: O(n)
// Time: O(n)

class Solution {
    private Map<Character, List<Integer>> cache = new HashMap<>();
    private Map<String, Integer> result = new HashMap<>();

    public int numMatchingSubseq(String s, String[] words) {
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            if (!cache.containsKey(s.charAt(i))) {
                cache.put(s.charAt(i), new ArrayList<>(Arrays.asList(i)));
            } else {
                cache.get(s.charAt(i)).add(i);
            }
        }
        for (String word : words) {
            if (result.containsKey(word)) {
                res += result.get(word);
                continue;
            }
            int tempRes = isSubsequence(word) ? 1 : 0;
            result.put(word, tempRes);
            res += tempRes;
        }
        return res;
    }

    private boolean isSubsequence(String s) {
        int tempIndex = -1;
        for (int i = 0; i < s.length(); i++) {
            if (!cache.containsKey(s.charAt(i))) {
                return false;
            }
            boolean flag = false;
            for (Integer index : cache.get(s.charAt(i))) {
                if (index > tempIndex) {
                    tempIndex = index;
                    flag = true;
                    break;
                }
            }
            if (!flag) return false;
        }
        return true;
    }
}




