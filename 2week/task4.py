"""https://leetcode.com/problems/zigzag-conversion/
submissions/1402232103?envType=problem-list-v2&envId=string"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        if numRows == 1:
            return s
        for i in range(numRows, 0, -1):
            j = numRows - i
            flag = 1
            while j < len(s):
                res += s[j]
                # if j+2*(numRows-i)<len(s) and numRows-i: res+=s[j+2*(numRows-i)]
                if (i - 1 and flag == 1) or not (numRows - i):
                    j += 2 * (i - 1)
                    flag = 2
                    if not (i - 1):
                        break
                elif (numRows - i and flag == 2) or not (i - 1):
                    j += 2 * (numRows - i)
                    flag = 1
        return res


a = Solution()
print(a.convert("A", 1))
