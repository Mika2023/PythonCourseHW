"""https://leetcode.com/problems/
longest-substring-of-all-vowels-in-order/
submissions/1474680187"""


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        start = end = 0
        vowel_to_next = {"a": "e", "e": "i", "i": "o", "o": "u", "u": "u"}
        longest_sub = 0

        while end < len(word):
            if start == end:
                if word[end] != "a":
                    start += 1
                end += 1
            else:
                prev = word[end - 1]
                if word[end] == prev or word[end] == vowel_to_next[prev]:
                    if word[end] == "u":
                        longest_sub = max(longest_sub, end - start + 1)
                    end += 1
                else:
                    start = end
        return longest_sub
