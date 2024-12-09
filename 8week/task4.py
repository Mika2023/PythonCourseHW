"""https://leetcode.com/problems/
frequency-of-the-most-frequent-element/
submissions/1474677767"""

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = end = len(nums) - 1
        area = 0

        while start:
            start -= 1
            area += nums[end] - nums[start]
            if k < area:
                diff = nums[end] - nums[end - 1]
                area -= diff * (end - start)
                end -= 1
        return end - start + 1
