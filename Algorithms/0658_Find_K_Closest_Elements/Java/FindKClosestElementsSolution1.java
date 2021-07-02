
// Space: O(n)
// Time: O(n)

class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> res = new ArrayList<>();
        if (arr.length == 0 || k == 0) return null;
        if (k >= arr.length) {
            for (int i : arr) {
                res.add(i);
            }
            return res;
        }
        int targetIndex = binarySearch(arr, x);
        int left = targetIndex - 1, right = targetIndex;
        while (res.size() < k) {
            if (0 <= left && left < arr.length && 0 <= right && right < arr.length) {
                if (Math.abs(arr[left] - x) <= Math.abs(arr[right] - x)) {
                    res.add(0, arr[left]);
                    left -= 1;
                } else if (Math.abs(arr[left] - x) > Math.abs(arr[right] - x)) {
                    res.add(arr[right]);
                    right += 1;
                }
            } else if (0 <= left && left < arr.length) {
                res.add(0, arr[left]);
                left -= 1;
            } else if (0 <= right && right < arr.length) {
                res.add(arr[right]);
                right += 1;
            }
        }
        return res;
    }

    private int binarySearch(int[] arr, int target) {
        int left = 0, right = arr.length;
        while (left < right) {
            int mid = (right + left) / 2;
            if (arr[mid] == target) {
                right = mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else if (arr[mid] > target) {
                right = mid;
            }
        }
        return left < arr.length ? left : left - 1;
    }
}




