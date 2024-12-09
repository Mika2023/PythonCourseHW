"""https://leetcode.com/problems/
maximum-sum-of-two-non-overlapping-subarrays/
submissions/1474658784"""

from typing import List


class Solution:
    def getMaxSubarraySum(self, arr: List[int], size: int) -> int:
        n = len(arr)
        if n < size:
            return 0
        maxi = temp = sum(arr[:size])
        for i in range(1, n - size + 1):
            temp = temp + arr[i + size - 1] - arr[i - 1]
            if temp > maxi:
                maxi = temp
        return maxi

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        summ = sum(nums[:firstLen])
        ans = summ + self.getMaxSubarraySum(nums[firstLen:], secondLen)
        for i in range(1, n - firstLen + 1):
            summ = summ + nums[i + firstLen - 1] - nums[i - 1]
            first_sum = self.getMaxSubarraySum(nums[:i], secondLen)
            second_sum = self.getMaxSubarraySum(nums[i + firstLen :], secondLen)
            sec_sum = first_sum if first_sum > second_sum else second_sum
            if summ + sec_sum > ans:
                ans = summ + sec_sum
        return ans
