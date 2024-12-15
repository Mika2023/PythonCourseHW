"""https://leetcode.com/problems/
binary-tree-right-side-view/submissions/1479456793"""

from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        null_next_arr = [root.val]

        queue = deque()
        queue.append(root)
        temp = TreeNode(-999)

        while queue:
            prev = temp
            for i in range(len(queue)):
                popped = queue.popleft()
                if popped.left:
                    queue.append(popped.left)
                    prev = popped.left
                if popped.right:
                    queue.append(popped.right)
                    prev = popped.right
            null_next_arr.append(prev.val)

        return null_next_arr[:-1]


a = Solution()
print(a.rightSideView(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))))
