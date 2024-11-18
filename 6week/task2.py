"""https://leetcode.com/problems/
repeated-dna-sequences/submissions/1454495403"""

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        res = []
        start = 0
        end = 9
        while end < len(s):
            substr = s[start:] if end == len(s) - 1 else s[start : end + 1]
            if substr in s[start + 1 :] and not (substr in res):
                res.append(substr)
            start += 1
            end += 1
        return res
