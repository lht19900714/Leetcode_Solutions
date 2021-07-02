
// Space: O(n)
// Time: O(n)

class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> res = new ArrayList<>();
        for (int i : arr) {
            res.add(i);
        }
        res.sort((a, b) -> Math.abs(a - x) - Math.abs(b - x));
        //res.sort(Comparator.comparingInt(a -> Math.abs(a - x)));
        res = res.subList(0, k);
        Collections.sort(res);
        return res;
    }
}




