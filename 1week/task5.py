"""https://leetcode.com/problems/count-and-say/submissions/1398936305?envType=problem-list-v2&envId=string"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.run_length(self.countAndSay(n - 1))

    def run_length(self, s: str) -> str:
        if len(s) == 1:
            return "1" + s[0]

        res = ""
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                res += str(count) + s[i - 1]
                count = 1
        res += str(count) + s[-1]
        return res


a = Solution()
print(a.countAndSay(3))
