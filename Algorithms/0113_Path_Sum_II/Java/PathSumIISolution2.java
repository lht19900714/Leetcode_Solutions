
// Space: O(n)
// Time: O(n)

class Solution {
    List<List<Integer>> res = null;

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if (root == null) return new ArrayList<>();
        res = new ArrayList<>();
        dfs(root, new ArrayList<>(), targetSum);
        return res;
    }

    private void dfs(TreeNode root, List<Integer> temp, int target) {
        temp.add(root.val);
        if (root.left == null && root.right == null) {
            if (temp.stream().mapToInt(Integer::intValue).sum() == target) {
                res.add(new ArrayList<>(temp));
            }
            temp.remove(temp.size() - 1);
            return;
        }
        if (root.left != null) dfs(root.left, temp, target);
        if (root.right != null) dfs(root.right, temp, target);
        temp.remove(temp.size() - 1);
    }
}




