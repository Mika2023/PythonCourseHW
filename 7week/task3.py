"""https://leetcode.com/problems/
binary-subarrays-with-sum/submissions/1474609370"""

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        curr_sum = 0
        res = 0

        for num in nums:
            curr_sum += num
            if curr_sum - goal in count:
                res += count[curr_sum - goal]
            count[curr_sum] = count.get(curr_sum, 0) + 1

        return res
