class node:
    def __init__(self):
        self.child = {}
        self.is_end = False

    def add_word(self, word):
        cur = self
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = node()
            cur = cur.child[ch]
        cur.is_end = True


class Solution:
    def findWords(self, board, words):
        root = node()

        for word in words:
            root.add_word(word)

        row, col = len(board), len(board[0])
        vis = set()
        res = set()

        def backtrack(r, c, path, cur):
            if r < 0 or c < 0 or r >= row or c >= col or (r, c) in vis:
                return

            ch = board[r][c]

            if ch not in cur.child:
                return

            vis.add((r, c))

            cur = cur.child[ch]
            path += ch

            if cur.is_end:
                res.add(path)

            backtrack(r - 1, c, path, cur)
            backtrack(r + 1, c, path, cur)
            backtrack(r, c - 1, path, cur)
            backtrack(r, c + 1, path, cur)

            vis.remove((r, c))

        for r in range(row):
            for c in range(col):
                backtrack(r, c, "", root)

        return list(res)