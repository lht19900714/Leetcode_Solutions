
// Space: O(n)
// Time: O(n)

class Trie {

    private TrieNode cache;

    public Trie() {
        cache = new TrieNode();
    }

    public void insert(String word) {
        TrieNode cur = cache;
        for (Character c : word.toCharArray()) {
            if (cur.children[c - 'a'] == null) {
                cur.children[c - 'a'] = new TrieNode();
            }
            cur = cur.children[c - 'a'];
        }
        cur.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode res = searchString(word);
        return res != null && res.isEnd;
    }

    public boolean startsWith(String prefix) {
        TrieNode res = searchString(prefix);
        return res != null;
    }

    private TrieNode searchString(String string) {
        TrieNode cur = cache;
        for (Character c : string.toCharArray()) {
            if (cur.children[c - 'a'] == null) return null;
            cur = cur.children[c - 'a'];
        }
        return cur;
    }
}

class TrieNode {
    TrieNode[] children;
    boolean isEnd;

    public TrieNode() {
        children = new TrieNode[26];
        isEnd = false;
    }
}





