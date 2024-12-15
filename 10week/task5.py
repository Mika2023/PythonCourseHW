"""https://leetcode.com/problems/
house-robber-iii/submissions/1479542635"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def findMax(cur: Optional[TreeNode]) -> List[int]:
            if not cur:
                return [0, 0]

            left_res = findMax(cur.left)
            right_res = findMax(cur.right)

            inc_cur = cur.val + left_res[1] + right_res[1]

            exc_cur = max(left_res[0], left_res[1]) + max(right_res[0], right_res[1])

            return [inc_cur, exc_cur]

        res = findMax(root)
        return max(res[0], res[1])
