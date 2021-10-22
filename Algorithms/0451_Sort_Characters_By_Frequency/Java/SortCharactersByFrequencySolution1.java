
// Space: O(n)
// Time: O(n)

public class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> counter = new HashMap<>();
        for (char c : s.toCharArray()) {
            counter.put(c, (counter.getOrDefault(c, 0)) + 1);
        }
        List<Character> list = new ArrayList<>();
        for (char c : s.toCharArray()) {
            list.add(c);
        }
        Collections.sort(list, (x1, x2) -> {
            int res = -(counter.get(x1) - counter.get(x2));
            if (res == 0) {
                return Character.compare(x1, x2);
            }
            return res;
        });
        StringBuilder sb = new StringBuilder();
        for (Character character : list) {
            sb.append(character);
        }
        return sb.toString();
    }
}




