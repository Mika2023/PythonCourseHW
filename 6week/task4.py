"""https://leetcode.com/problems/permutation-in-string/
submissions/1456072932"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == len(s2) and len(s1) == 1:
            return s1 == s2
        if len(s1) == 1:
            return s1 in s2

        start = 0
        end = len(s1) - 1
        while end < len(s2):
            for i in range(len(s1)):
                if (s1[i] not in s2[start : end + 1]) or (
                    s2[start : end + 1].count(s1[i]) != s1.count(s1[i])
                ):
                    break
            else:
                return True
            start += 1
            end += 1

        return False


a = Solution()
print(a.checkInclusion("hello", "ooolleoooleh"))
