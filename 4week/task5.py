"""https://leetcode.com/problems/
kth-largest-element-in-an-array/
submissions/1421888834?envType=problem-list-v2&envId=array"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
