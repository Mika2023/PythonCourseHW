"""https://leetcode.com/problems/surrounded-regions/
submissions/1421863912?envType=problem-list-v2&envId=array"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if self.dfs(board, i, j):
                        self.replaceEl(board, "x", "X")
                    else:
                        self.replaceEl(board, "x", "o")
        self.replaceEl(board, "o", "O")

    def dfs(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False  # the region is not surrounded
        if board[i][j] != "O":
            return True
        board[i][j] = "x"
        res1 = self.dfs(board, i + 1, j)
        res2 = self.dfs(board, i - 1, j)
        res3 = self.dfs(board, i, j + 1)
        res4 = self.dfs(board, i, j - 1)
        return res1 and res2 and res3 and res4

    def replaceEl(self, board, old, new):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == old:
                    board[i][j] = new
