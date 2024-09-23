"""https://leetcode.com/problems/string-to-integer-atoi/submissions/1392393335?envType=problem-list-v2&envId=string"""


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        if not len(s):
            return 0
        is_positive = True
        if s[0] == "-" or s[0] == "+":
            is_positive = False if s[0] == "-" else True
            s = s[1:]
        res = count = 0
        while s[count] in "0123456789":
            if res * 10 + ord(s[count]) - 48 >= 2**31 - 1:
                if is_positive:
                    res = 2**31 - 1
                elif res * 10 + ord(s[count]) - 48 != 2**31 - 1:
                    res = 2**31
                break
            res = res * 10 + ord(s[count]) - 48
            count += 1
            if count >= len(s):
                break
        res *= (-1) if not is_positive else 1
        return res


a = Solution()
print(a.myAtoi("words and 987"))
