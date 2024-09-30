"""https://leetcode.com/problems/
fraction-to-recurring-decimal/submissions/
1402176266?envType=problem-list-v2&envId=string"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""

        if numerator * denominator < 0:
            res += "-"
            if numerator < 0:
                numerator *= -1
            else:
                denominator *= -1
        elif numerator * denominator > 0 and numerator < 0:
            numerator *= -1
            denominator *= -1

        start_num = numerator
        ost = numerator % denominator
        prev = []
        res += str(numerator // denominator)
        if ost:
            res += "."
            if ost != denominator:
                numerator = ost * 10
                prev.append(ost)
            else:
                numerator *= 10

        while ost:
            res += str(numerator // denominator)
            ost = numerator % denominator
            if ost != denominator:
                numerator = ost * 10
            else:
                numerator *= 10

            if ost in prev:
                difference = len(prev) - prev.index(ost)
                res = (
                    res[: len(res) - difference]
                    + "("
                    + res[len(res) - difference : len(res)]
                    + ")"
                )
                break
            else:
                prev.append(ost)
            # if not ("." in res) and ost:
            #     if not ("." in res): res+="."
            #     numerator*=10
            # else: numerator = ost*10

            # if ost in prev:
        return res


a = Solution()
print(a.fractionToDecimal(4, 333))
