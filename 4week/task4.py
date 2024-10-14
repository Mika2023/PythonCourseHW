"""https://leetcode.com/problems/maximum-gap/
submissions/1421886533?envType=problem-list-v2&envId=array"""

from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i - 1])
        return max_gap
