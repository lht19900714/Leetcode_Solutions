
// Space: O(n)
// Time: O(n)

class MapSum {

    private Map<String, Integer> numberMap;
    private Map<String, List<String>> prefixMap;

    public MapSum() {
        numberMap = new HashMap<>();
        prefixMap = new HashMap<>();
    }

    public void insert(String key, int val) {
        if (!numberMap.containsKey(key)) {
            for (int i = 1; i < key.length() + 1; i++) {
                prefixMap.computeIfAbsent(key.substring(0, i), (k) -> new ArrayList<>()).add(key);
            }
        }
        numberMap.put(key, val);
    }

    public int sum(String prefix) {
        int res = 0;
        if (prefixMap.containsKey(prefix)) {
            for (String s : prefixMap.get(prefix)) {
                res += numberMap.get(s);
            }
        }
        return res;
    }
}




