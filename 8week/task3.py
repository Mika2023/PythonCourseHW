"""https://leetcode.com/problems/
longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
submissions/1474672405"""

from sortedcontainers import SortedList  # type: ignore
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = SortedList()
        left = right = ans = 0
        n = len(nums)
        while right < n:
            l.add(nums[right])
            while left <= right and l[-1] - l[0] > limit:
                l.remove(nums[left])
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
