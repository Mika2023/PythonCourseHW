"""https://leetcode.com/problems/
minimum-size-subarray-sum/submissions/1456100471"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        sum = 0
        min_len = len(nums) + 1
        left = 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1

        return min_len if min_len <= len(nums) else 0
