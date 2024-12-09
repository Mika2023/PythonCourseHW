"""https://leetcode.com/problems/
grumpy-bookstore-owner/submissions/1474665157"""

from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)

        initial = 0
        for i in range(n):
            if grumpy[i] == 0:
                initial += customers[i]

        max_add_satisfaction = 0
        cur_add_satisfaction = 0

        for i in range(minutes):
            if grumpy[i] == 1:
                cur_add_satisfaction += customers[i]

        max_add_satisfaction = cur_add_satisfaction

        for i in range(minutes, n):
            if grumpy[i] == 1:
                cur_add_satisfaction += customers[i]
            if grumpy[i - minutes] == 1:
                cur_add_satisfaction -= customers[i - minutes]

            max_add_satisfaction = max(max_add_satisfaction, cur_add_satisfaction)

        return initial + max_add_satisfaction
