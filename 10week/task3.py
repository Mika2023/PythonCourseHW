"""https://leetcode.com/problems/
lowest-common-ancestor-of-a-binary-search-tree/
submissions/1479501372"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def findPath(cur: "TreeNode", dest: "TreeNode", path: List[int]):

            path.append(cur)

            if dest.val == cur.val:
                return

            if cur.val > dest.val:
                findPath(cur.left, dest, path)
            else:
                findPath(cur.right, dest, path)

        path_p = []
        findPath(root, p, path_p)

        path_q = []
        findPath(root, q, path_q)

        common = list(set(path_q).intersection(path_p))
        return common[-1]


a = Solution()
print(
    a.lowestCommonAncestor(
        root=TreeNode(
            6,
            TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
            TreeNode(8, TreeNode(7), TreeNode(9)),
        ),
        p=TreeNode(2),
        q=TreeNode(4),
    )
)
