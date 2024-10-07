"""https://leetcode.com/problems/minimum-path-sum/
submissions/1411930094?envType=problem-list-v2&envId=array"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        copy_grid = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    copy_grid[i][j] = grid[i][j]
                elif i == 0:
                    copy_grid[i][j] = grid[i][j] + copy_grid[i][j - 1]
                elif j == 0:
                    copy_grid[i][j] = grid[i][j] + copy_grid[i - 1][j]
                else:
                    copy_grid[i][j] = grid[i][j] + min(
                        copy_grid[i - 1][j], copy_grid[i][j - 1]
                    )
        return copy_grid[-1][-1]
