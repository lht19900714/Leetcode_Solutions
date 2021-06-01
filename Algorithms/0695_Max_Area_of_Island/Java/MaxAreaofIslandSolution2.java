
// Space: O(n)
// Time: O(n)

class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int res = 0;
        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                if (grid[y][x] == 1) {
                    Stack<int[]> stack = new Stack<>();
                    int tempRes = 0;
                    grid[y][x] = 0;
                    stack.add(new int[]{y, x});
                    while (!stack.empty()) {
                        int[] cur = stack.pop();
                        tempRes += 1;
                        if (0 <= cur[0] - 1 && cur[0] - 1 < m && 0 <= cur[1] && cur[1] < n && grid[cur[0] - 1][cur[1]] == 1) {
                            grid[cur[0] - 1][cur[1]] = 0;
                            stack.add(new int[]{cur[0] - 1, cur[1]});
                        }
                        if (0 <= cur[0] + 1 && cur[0] + 1 < m && 0 <= cur[1] && cur[1] < n && grid[cur[0] + 1][cur[1]] == 1) {
                            grid[cur[0] + 1][cur[1]] = 0;
                            stack.add(new int[]{cur[0] + 1, cur[1]});
                        }
                        if (0 <= cur[0] && cur[0] < m && 0 <= cur[1] - 1 && cur[1] - 1 < n && grid[cur[0]][cur[1] - 1] == 1) {
                            grid[cur[0]][cur[1] - 1] = 0;
                            stack.add(new int[]{cur[0], cur[1] - 1});
                        }
                        if (0 <= cur[0] && cur[0] < m && 0 <= cur[1] + 1 && cur[1] + 1 < n && grid[cur[0]][cur[1] + 1] == 1) {
                            grid[cur[0]][cur[1] + 1] = 0;
                            stack.add(new int[]{cur[0], cur[1] + 1});
                        }
                    }
                    res = Math.max(res, tempRes);
                }
            }
        }
        return res;
    }
}





