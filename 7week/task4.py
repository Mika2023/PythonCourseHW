"""https://leetcode.com/problems/
fruit-into-baskets/submissions/1474652201"""

from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if fruits.count(fruits[0]) == len(fruits) or len(set(fruits)) == 2:
            return len(fruits)

        fruit_type1 = fruit_type2 = end1 = end2 = -1

        l = len(fruits)
        right = left = 0
        res = right - left + 1
        while right < l:
            if fruit_type1 == -1:
                fruit_type1 = fruits[right]
                end1 = right
            elif fruit_type2 == -1 and fruit_type1 != fruits[right]:
                fruit_type2 = fruits[right]
                end2 = right
            elif fruits[right] == fruit_type1 or fruits[right] == fruit_type2:
                end1 = (
                    end1
                    if fruits[right] == fruit_type2 and fruit_type2 != -1
                    else right
                )
                end2 = end2 if fruits[right] == fruit_type1 else right
                right += 1
                continue
            else:
                res = max(res, right - left)
                if end1 < end2:
                    left = end1 + 1
                    fruit_type1 = fruits[right]
                    end1 = right
                else:
                    left = end2 + 1
                    fruit_type2 = fruits[right]
                    end2 = right

            right += 1

        res = max(res, right - left)
        return res


a = Solution()
print(a.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
