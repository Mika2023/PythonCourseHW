"""https://leetcode.com/problems/sort-colors/
submissions/1411892901?envType=problem-list-v2&envId=array"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        temp = [0, 0, 0]
        for i in range(len(nums)):
            temp[nums[i]] += 1
        color = i = 0
        while color < 3:
            if temp[color] > 0:
                nums[i] = color
                temp[color] -= 1
                i += 1
            else:
                color += 1
