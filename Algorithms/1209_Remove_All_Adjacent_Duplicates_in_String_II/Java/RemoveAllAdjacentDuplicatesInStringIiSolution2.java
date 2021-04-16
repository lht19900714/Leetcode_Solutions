
// Space: O(n)
// Time: O(n)

class Solution {
    public String removeDuplicates(String s, int k) {
        if (s.length() <= 1) return s;
        if (s.length() < k) return s;

        Stack<Pair<Character, Integer>> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (stack.size() == 0 || (stack.size() > 0 && stack.peek().getKey() != c)) {
                Pair<Character, Integer> newItem = new Pair<>(c, 1);
                stack.add(newItem);
            } else if (stack.peek().getKey() == c) {
                Pair<Character, Integer> top = stack.pop();
                int count = top.getValue();
                count++;
                if (count < k) {
                    stack.add(new Pair<Character, Integer>(top.getKey(), count));
                }
            }
        }

        StringBuilder res = new StringBuilder();
        while (stack.size() > 0) {
            Pair<Character, Integer> temp = stack.pop();
            int count = temp.getValue();
            while (count-- > 0) {
                res.append(temp.getKey());
            }
        }
        return res.reverse().toString();
    }
}








