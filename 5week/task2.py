"""https://leetcode.com/problems/
longest-consecutive-sequence/submissions/1429609254"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 1
        current = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        return longest
