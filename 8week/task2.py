"""https://leetcode.com/problems/
swap-for-longest-repeated-character-substring/
submissions/1474669147"""

from cmath import inf
from collections import defaultdict


class Solution:
    def maxRepOpt1(self, s: str) -> int:
        pos = defaultdict(lambda: [inf, -inf])
        for i, c in enumerate(s):
            pos[c] = [min(pos[c][0], i), max(pos[c][1], i)]
        freq = defaultdict(int)
        max_len = 1
        left = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            while len(freq) > 2 or len(freq) == 2 and min(freq.values()) > 1:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            max_char = max(freq.keys(), key=lambda x: freq[x])
            max_len = max(
                max_len,
                freq[max_char] + (pos[max_char][0] < left or right < pos[max_char][1]),
            )
        return max_len
