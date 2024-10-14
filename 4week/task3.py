"""https://leetcode.com/problems/
find-minimum-in-rotated-sorted-array/submissions/
1421882147?envType=problem-list-v2&envId=array"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = nums[-1]
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[low]:
                low = mid
            else:
                high = mid
        return nums[mid]
