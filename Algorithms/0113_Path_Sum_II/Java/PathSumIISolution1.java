
// Space: O(n)
// Time: O(n)

class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if (root == null) return new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        Queue<List<Object>> queue = new ArrayDeque<>();

        List<Object> temp = new ArrayList<>();
        temp.add(root);
        temp.add(new ArrayList<>(Arrays.asList(root.val)));
        queue.add(temp);

        while (!queue.isEmpty()) {
            List<Object> cur = queue.poll();
            TreeNode curRoot = (TreeNode) cur.get(0);
            ArrayList<Integer> curList = (ArrayList) cur.get(1);
            if (curRoot.left == null && curRoot.right == null) {
                if (curList.stream().mapToInt(Integer::intValue).sum() == targetSum) {
                    res.add(curList);
                }
            }
            if (curRoot.left != null) {
                List<Object> temp1 = new ArrayList<>();
                temp1.add(curRoot.left);
                List<Integer> tempNum = new ArrayList<>(curList);
                tempNum.add(curRoot.left.val);
                temp1.add(tempNum);
                queue.add(temp1);
            }
            if (curRoot.right != null) {
                List<Object> temp1 = new ArrayList<>();
                temp1.add(curRoot.right);
                List<Integer> tempNum = new ArrayList<>(curList);
                tempNum.add(curRoot.right.val);
                temp1.add(tempNum);
                queue.add(temp1);
            }
        }
        return res;
    }
}





