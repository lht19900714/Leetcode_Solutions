
// Space: O(n)
// Time: O(n^2)

class Solution {
    public int maxProduct(String[] words) {
        int res = 0;
        for (int i = 0; i < words.length - 1; i++) {
            Set<Character> temp = new HashSet<>();
            for (char c : words[i].toCharArray()) {
                temp.add(c);
            }
            for (int j = i + 1; j < words.length; j++) {
                boolean isContain = false;
                for (char c : words[j].toCharArray()) {
                    if (temp.contains(c)) {
                        isContain = true;
                        break;
                    }
                }
                if (!isContain) res = Math.max(res, words[i].length() * words[j].length());
            }
        }
        return res;
    }
}



       

