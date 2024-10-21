"""https://leetcode.com/problems/
random-pick-index/submissions/1429668597"""

from typing import List
import random as rd


class Solution:

    def __init__(self, nums: List[int]):
        nums.sort()
        nums_set = set(nums)
        self.keys_indexes = {key_item: [] for key_item in nums_set}
        for i in range(len(nums)):
            self.keys_indexes[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return rd.choice(self.keys_indexes[target])
