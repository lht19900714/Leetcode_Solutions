
// Space: O(n)
// Time: O(n)

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 1){
            List res = new ArrayList<>();
            res.add(Arrays.asList(strs));
        }
        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> cache = new HashMap<>();
        for (String s : strs) {
            String key = generateKey(s);
            cache.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        for (String key : cache.keySet()) {
            res.add(cache.get(key));
        }
        return res;
    }

    private String generateKey(String str) {
        char[] chars = str.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }
}




