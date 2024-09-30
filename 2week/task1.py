"""https://leetcode.com/problems/
edit-distance/submissions/
1401710672?envType=problem-list-v2&envId=string"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        alg_tab = [[i] * (n2 + 1) for i in range(n1 + 1)]
        for i in range(n2 + 1):
            alg_tab[0][i] = i

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word2[j - 1] == word1[i - 1]:
                    alg_tab[i][j] = alg_tab[i - 1][j - 1]
                else:
                    alg_tab[i][j] = (
                        min(alg_tab[i - 1][j - 1], alg_tab[i - 1][j], alg_tab[i][j - 1])
                        + 1
                    )
        return alg_tab[n1][n2]
