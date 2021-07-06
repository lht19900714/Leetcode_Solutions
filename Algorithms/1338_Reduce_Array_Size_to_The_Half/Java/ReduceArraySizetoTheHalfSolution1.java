
// Space: O(n)
// Time: O(n)

class Solution {
    public int minSetSize(int[] arr) {
        Map<Integer, Integer> counter = new HashMap<>();
        List<Integer> tempList = new ArrayList<>();
        int res = arr.length, resCount = 0;

        for (int i : arr) {
            if (counter.containsKey(i)) {
                counter.put(i, counter.get(i) + 1);
            } else {
                counter.put(i, 1);
                tempList.add(i);
            }
        }
        tempList.sort((x1, x2) -> counter.get(x2) - counter.get(x1));

        for (int i : tempList) {
            resCount += 1;
            res -= counter.get(i);
            if (res <= arr.length / 2) return resCount;
        }
        return resCount;
    }
}




