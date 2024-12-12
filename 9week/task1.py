"""https://leetcode.com/problems/
recover-binary-search-tree/submissions/1477146152"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        wrong_pairs = []
        prev = None
        self.inorder(root, prev, wrong_pairs)
        a, b = self.get_violated_pairs(wrong_pairs)

        a.val, b.val = b.val, a.val

    def get_violated_pairs(self, wrong_pairs):
        node1, node2 = None, None
        if len(wrong_pairs) == 1:
            node1, node2 = wrong_pairs[0]
        else:
            node1, node2 = wrong_pairs[0][0], wrong_pairs[1][1]

        return node1, node2

    def inorder(self, node, prev, wrong_pairs):
        if node:
            self.inorder(node.left, prev, wrong_pairs)
            if prev and node.val < prev.val:
                wrong_pairs.append((prev, node))
            prev = node
            self.inorder(node.right, prev, wrong_pairs)


a = Solution()
root = TreeNode(1, TreeNode(3, None, TreeNode(2)), None)
a.recoverTree(root)
