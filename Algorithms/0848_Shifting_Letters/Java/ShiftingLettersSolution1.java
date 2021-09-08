
// Space: O(1)
// Time: O(n)

class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        int total = Arrays.stream(shifts).map(x -> x % 26).sum();
        char[] res = new char[s.length()];

        for (int i = 0; i < s.length(); i++) {
            int index = s.charAt(i) - 'a';
            res[i] = (char) (97 + (index + total) % 26);
            total = Math.floorMod(total - shifts[i], 26);
        }
        return new String(res);
    }
}




