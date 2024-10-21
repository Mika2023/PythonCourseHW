"""https://leetcode.com/problems/
set-matrix-zeroes/submissions/1429567670"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        flag = False

        for i in range(len(matrix)):
            if 0 in matrix[i]:
                while 0 in matrix[i]:
                    ind = matrix[i].index(0)
                    matrix[0][ind] = True
                    if i != 0:
                        matrix[i][ind] = 1
                if i != 0:
                    matrix[i] = [0 for _ in range(n)]
                else:
                    flag = True

        for i in range(n):
            if type(matrix[0][i]) == bool and matrix[0][i]:
                for j in range(len(matrix)):
                    matrix[j][i] = 0

        if flag:
            matrix[0] = [0 for _ in range(n)]

        print(matrix)


a = Solution()
a.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
