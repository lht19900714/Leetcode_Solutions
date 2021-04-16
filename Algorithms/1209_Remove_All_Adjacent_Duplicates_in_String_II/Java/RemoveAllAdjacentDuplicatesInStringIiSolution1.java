
// Space: O(n)
// Time: O(n)

class Solution {
    public String removeDuplicates(String s, int k) {
        if (s.length() <= 1) return s;
        if (s.length() < k) return s;

        Stack<Character> stackChar = new Stack<>();
        Stack<Integer> stackCharCount = new Stack<>();
        for (Character c : s.toCharArray()) {
            if ((stackChar.size() > 0 && c != stackChar.peek()) || stackChar.size() == 0) {
                stackChar.add(c);
                stackCharCount.add(1);
            } else if (c == stackChar.peek()) {
                stackCharCount.add(stackCharCount.pop() + 1);
            }

            while (stackCharCount.size() > 0 && stackCharCount.peek() >= k) {
                int temp = stackCharCount.pop();
                while (temp >= k) {
                    temp -= k;
                }
                if (temp == 0) {
                    stackChar.pop();
                } else {
                    stackCharCount.add(temp);
                }
            }
        }

        StringBuilder res = new StringBuilder();
        while (stackChar.size() > 0) {
            Character chr = stackChar.pop();
            Integer integer = stackCharCount.pop();
            StringBuilder tempRes = new StringBuilder();
            for (int i = 0; i < integer; i++) {
                tempRes.append(chr);
            }
            res.append(tempRes);
        }
        return res.reverse().toString();
}









