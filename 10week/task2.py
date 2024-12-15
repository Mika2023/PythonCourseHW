"""https://leetcode.com/problems/
kth-smallest-element-in-a-bst/submissions/1479480569"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1

        def inorder(cur: Optional[TreeNode]):
            nonlocal count
            if not cur:
                return -1

            res = inorder(cur.left)
            if res != -1:
                return res

            if count == k:
                return cur.val
            else:
                count += 1

            res = inorder(cur.right)
            if res != -1:
                return res
            return -1

        return inorder(root)

        # prev = TreeNode(-1)
        # cur = root

        # small_arr = [root.val]
        # while cur.left or cur.right:
        #     if cur.left:
        #         prev = cur
        #         cur = cur.left
        #     elif cur.right:
        #         prev = cur
        #         cur = cur.right

        #     small_arr.append(prev.val)

        # return small_arr[len(small_arr)-k]


a = Solution()
print(a.kthSmallest(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1))
