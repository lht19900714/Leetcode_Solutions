
# Space: O(n)
# Time: O(n)


import collections


class Solution():
    def findWords(self, board, words):
        column = len(board)
        if column == 0: return []
        row = len(board[0])
        if row == 0: return []

        target_word = set()
        res = set()

        # build a trie, this will be used in DFS search
        trie = collections.defaultdict(set)
        trie[''] = {word[0] for word in words}
        for each_word in words:
            string = ''
            for index in range(len(each_word)):
                string += each_word[index]
                if index != len(each_word) - 1:
                    trie[string].add(each_word[index + 1])
                else:
                    target_word.add(each_word)


        def search(word_list, cur_sub_string, x, y):
            if cur_sub_string in target_word:
                res.add(cur_sub_string)
                target_word.remove(cur_sub_string)

            if (not 0 <= x < row) or (not 0 <= y < column) or board[y][x] == 0 or board[y][x] not in trie[cur_sub_string] or len(res) == len(word_list): return

            cur_sub_string += board[y][x]
            temp = board[y][x]
            board[y][x] = 0
            search(word_list, cur_sub_string, x - 1, y)
            search(word_list, cur_sub_string, x + 1, y)
            search(word_list, cur_sub_string, x, y - 1)
            search(word_list, cur_sub_string, x, y + 1)
            board[y][x] = temp
            cur_sub_string = cur_sub_string[:-1]


        for y in range(column):
            for x in range(row):
                if len(words) == len(res):
                    return res
                search(words, '', x, y)

        return res




