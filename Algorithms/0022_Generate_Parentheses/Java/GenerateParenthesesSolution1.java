
// Space: O(n)
// Time: O(n)

class Solution {
    private Set<String> res = new HashSet<>();

    public List<String> generateParenthesis(int n) {
        if (n == 0) return new ArrayList<>();
        if (n == 1) return Arrays.asList("()");

        dfs(n, n, "");
        return new ArrayList<>(res);
    }

    private void dfs(int left, int right, String tempRes) {
        if (left == right && left == 0) {
            if (verify(tempRes)) {
                res.add(tempRes);
            }
            return;
        }
        if (left > 0 && left <= right) {
            tempRes += "(";
            dfs(left - 1, right, tempRes);
            tempRes = tempRes.substring(0, tempRes.length() - 1);
            tempRes += ")";
            dfs(left, right - 1, tempRes);
            tempRes = tempRes.substring(0, tempRes.length() - 1);
        }
        if (left == 0) {
            tempRes += ")";
            dfs(left, right - 1, tempRes);
            tempRes = tempRes.substring(0, tempRes.length() - 1);
        }
    }

    private boolean verify(String str) {
        int count = 0;
        for (char c : str.toCharArray()) {
            if (c == '(') count++;
            else if (c == ')') count--;
            if (count < 0) return false;
        }
        return count == 0;
    }




