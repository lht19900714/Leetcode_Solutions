
// Space: O(1)
// Time: O(n)

class Solution {
    public int fib(int n) {
        if (n <= 1) return n;
        int counter = 1, a = 0, b = 1, temp;
        while (counter++ != n) {
            temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
}




