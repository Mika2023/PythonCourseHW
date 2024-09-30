"""https://leetcode.com/problems/
word-search/submissions/
1404207428?envType=problem-list-v2&envId=string"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        indexes = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    indexes.append([i, j, 0])

        if not len(indexes):
            return False
        elif len(word) == 1:
            return True

        for i in range(len(indexes)):
            if self.recourse(board, 1, word, indexes[i][0], indexes[i][1]):
                return True

        return False

        # for i in range(len(indexes)):
        #     pos_i = indexes[i][0]
        #     pos_j = indexes[i][1]
        #     copy_board = deepcopy(board)
        #     for j in range(1,len(word)):
        #         copy_board[pos_i][pos_j] = ""
        #         if pos_i>0 and copy_board[pos_i-1][pos_j]==word[j]: indexes.append([pos_i-1,pos_j])
        #         elif pos_i<len(copy_board)-1 and copy_board[pos_i+1][pos_j]==word[j]: indexes.append([pos_i+1,pos_j])
        #         elif pos_j>0 and copy_board[pos_i][pos_j-1]==word[j]: indexes.append([pos_i,pos_j-1])
        #         elif pos_j<len(copy_board[0])-1 and copy_board[pos_i][pos_j+1]==word[j]: indexes.append([pos_i,pos_j+1])
        #         else: break
        #     else: return True
        # return False

        # while len(indexes):
        #     pres = indexes.pop()
        #     pos_i,pos_j,j = pres[0],pres[1],pres[2]
        #     temp = len(indexes)
        #     if pos_i>0 and board[pos_i-1][pos_j]==word[j+1]: indexes.append([pos_i-1,pos_j,j+1])
        #     if pos_i<len(board)-1 and board[pos_i+1][pos_j]==word[j+1]: indexes.append([pos_i+1,pos_j,j+1])
        #     if pos_j>0 and board[pos_i][pos_j-1]==word[j+1]: indexes.append([pos_i,pos_j-1,j+1])
        #     if pos_j<len(board[0])-1 and board[pos_i][pos_j+1]==word[j+1]: indexes.append([pos_i,pos_j+1,j+1])
        #     if len(indexes)==temp: continue
        #     board[pos_i][pos_j] = ""
        #     if j+1==len(word)-1: return True
        # return False

    def recourse(
        self, board: List[List[str]], next_ind: int, word: str, pos_i: int, pos_j: int
    ):
        if next_ind == len(word):
            return True

        indexes = []
        if pos_i > 0 and board[pos_i - 1][pos_j] == word[next_ind]:
            indexes.append([pos_i - 1, pos_j])
        if pos_i < len(board) - 1 and board[pos_i + 1][pos_j] == word[next_ind]:
            indexes.append([pos_i + 1, pos_j])
        if pos_j > 0 and board[pos_i][pos_j - 1] == word[next_ind]:
            indexes.append([pos_i, pos_j - 1])
        if pos_j < len(board[0]) - 1 and board[pos_i][pos_j + 1] == word[next_ind]:
            indexes.append([pos_i, pos_j + 1])

        if not len(indexes):
            return False

        for i in range(len(indexes)):
            board[pos_i][pos_j] = ""
            res = self.recourse(board, next_ind + 1, word, indexes[i][0], indexes[i][1])
            if res:
                return True

        board[pos_i][pos_j] = word[next_ind - 1]
        return False


a = Solution()
print(
    a.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    )
)
