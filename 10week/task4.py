"""я бы добавила сюда линк с accepted, нооооооооо
каким-то образом тесты играют с моим кодом
 в русскую рулетку и то проходят, то нет(
https://leetcode.com/problems/
lowest-common-ancestor-of-a-binary-tree/submissions/1479529981
пройдено 24 теста из 32
https://leetcode.com/problems/
lowest-common-ancestor-of-a-binary-tree/submissions/1479531694
пройдено 23 теста из 32
К А К
"""

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
            if not cur:
                return False
            if not (cur.left or cur.right):
                if cur.val != dest.val:
                    return False

                path.append(cur)
                return True

            path.append(cur)

            if dest.val == cur.val:
                return True

            if not (findPath(cur.left, dest, path) or findPath(cur.right, dest, path)):
                path.pop()

        path_p = []
        findPath(root, p, path_p)

        path_q = []
        findPath(root, q, path_q)

        common = list(set(path_q).intersection(path_p))
        return common[-1].val


a = Solution()
print(
    a.lowestCommonAncestor(
        root=TreeNode(
            -1, TreeNode(0, TreeNode(-2), TreeNode(4, TreeNode(8))), TreeNode(3)
        ),
        p=TreeNode(8),
        q=TreeNode(0),
    )
)
