
// Space: O(n)
// Time: O(2^n)

class Solution {
    private Map<Character, Integer> cache = new HashMap<>();

    public int maxLength(List<String> arr) {
        if (arr.size() == 1) return arr.get(0).length();
        for (int i = 97; i < 97 + 26; i++) {
            cache.put((char) i, 1);
        }
        return backTracking(arr,0,0,0,false);
    }

    private int backTracking(List<String> arr, int curIndex, int tempCount, int res, boolean flag) {
        res = Math.max(res, tempCount);

        for (int i = curIndex; i < arr.size(); i++) {
            for (Character c : arr.get(i).toCharArray()) {
                cache.put(c, cache.get(c) - 1);
                if (cache.get(c) < 0) flag = true;
            }
            if (!flag) {
                tempCount += arr.get(i).length();
                res = backTracking(arr, i + 1, tempCount, res, flag);
                tempCount -= arr.get(i).length();
            }
            for (Character c : arr.get(i).toCharArray()) {
                cache.put(c, cache.get(c) + 1);
            }
            flag = false;
        }
        return res;
    }
}




