
// Space: O(n)
// Time: O(n)

class Solution {
    private int row;
    private int column;
    private List<String> res = new ArrayList<>();
    private Map<String, List<Character>> trie = new HashMap<>();
    private Set<String> targetWords = new HashSet<>();

    public List<String> findWords(char[][] board, String[] words) {
        column = board.length;
        row = board[0].length;
        for (String s : words) {
            trie.computeIfAbsent("", key -> new ArrayList<>()).add(s.charAt(0));
        }
        for (String word : words) {
            StringBuilder prefix = new StringBuilder("");
            for (int i = 0; i < word.length(); i++) {
                prefix.append(word.charAt(i));
                if (i < word.length() - 1) {
                    trie.computeIfAbsent(prefix.toString(), key -> new ArrayList<>()).add(word.charAt(i + 1));
                } else {
                    targetWords.add(prefix.toString());
                }
            }
        }
        for (int y = 0; y < column; y++) {
            for (int x = 0; x < row; x++) {
                dfs(board, new StringBuilder(), x, y, words);
            }
        }
        return res;
    }

    private void dfs(char[][] board, StringBuilder curStr, int x, int y, String[] words) {
        if (targetWords.contains(curStr.toString())) {
            res.add(curStr.toString());
            targetWords.remove(curStr.toString());
        }
        if (x < 0 || x >= row || y < 0 || y >= column || board[y][x] == '*' || !trie.getOrDefault(curStr.toString(), new ArrayList<>()).contains(board[y][x]) || words.length == res.size())
            return;
        // String temp = String.valueOf(board[y][x]);
        char temp = board[y][x];
        curStr.append(temp);
        board[y][x] = '*';
        dfs(board, curStr, x + 1, y, words);
        dfs(board, curStr, x - 1, y, words);
        dfs(board, curStr, x, y + 1, words);
        dfs(board, curStr, x, y - 1, words);
        board[y][x] = temp;
        curStr.deleteCharAt(curStr.length() - 1);
    }
}



