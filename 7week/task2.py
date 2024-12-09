"""https://leetcode.com/problems/
longest-substring-with-at-least-k-repeating-characters/
submissions/1474588514"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


a = Solution()
a.longestSubstring("aaabb", 3)
