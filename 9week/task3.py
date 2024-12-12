"""https://leetcode.com/problems/
path-sum-ii/submissions/1477233472"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        paths = []
        path = []

        def preorder(node: Optional[TreeNode], cur_sum: int, path: List[int]):
            if node == None:
                return

            cur_sum += node.val
            if cur_sum == targetSum and not (node.right != None or node.left != None):
                path.append(node.val)
                paths.append(path.copy())
                path.pop()
                return
            if node.right != None or node.left != None:
                path.append(node.val)
                preorder(node.left, cur_sum, path)
                preorder(node.right, cur_sum, path)
                path.pop()

        preorder(root, 0, path)
        return paths


a = Solution()
root = TreeNode(
    7, TreeNode(0, TreeNode(-1, None, TreeNode(1, None, TreeNode(-7))), TreeNode(-6))
)
print(a.pathSum(root, 0))
