
// Space: O(n)
// Time: O(n)

class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Map<String, List<String>> cache = new HashMap<>();
        List<List<String>> res = new ArrayList<>();
        for (String word : products) {
            for (int i = 1; i <= word.length(); i++) {
                if (cache.containsKey(word.substring(0, i))) cache.get(word.substring(0, i)).add(word);
                else cache.put(word.substring(0, i), new ArrayList<>(Arrays.asList(word)));
            }
        }
        for (int i = 1; i <= searchWord.length(); i++) {
            List<String> temp = cache.getOrDefault(searchWord.substring(0, i), new ArrayList<>());
            if (temp.size() != 0) {
                temp.sort(String::compareTo);
                if (temp.size() > 3) temp = temp.subList(0, 3);
            }
            res.add(temp);
        }
        return res;
    }
}





