"""https://leetcode.com/problems/
top-k-frequent-elements/submissions/1429652953"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        arr_freq = {}
        i = 0
        while i < len(nums):
            count = nums.count(nums[i])
            arr_freq[nums[i]] = count
            i += count

        arr_freq = {
            key: item
            for key, item in sorted(
                arr_freq.items(), key=lambda el: el[1], reverse=True
            )
        }

        return list(arr_freq.keys())[:k]
