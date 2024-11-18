"""https://leetcode.com/problems/
longest-substring-without-repeating-characters/
submissions/1392288450?envType=problem-list-v2&envId=string"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not (len(s)):
            return 0

        count = max_count = 1
        for i in range(1, len(s)):
            if s[i] in s[i - count : i]:
                max_count = count if count > max_count else max_count
                ind = s[i - count : i].find(s[i])
                count = count - ind - 1
            count += 1
        max_count = count if count > max_count else max_count
        return max_count


a = Solution()
print(a.lengthOfLongestSubstring(s="pwwkew"))
