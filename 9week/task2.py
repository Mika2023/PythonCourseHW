"""https://leetcode.com/problems/
construct-binary-tree-from-preorder-and-inorder-traversal/
submissions/1477181365"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_ind_dict = {inorder[i]: i for i in range(len(inorder))}

        def buildTreeNode(preorder, inorder_start, inorder_end):
            if not preorder or inorder_start < 0 or inorder_end > len(inorder):
                return None

            root_val = preorder[0]
            root_inorder_idx = val_ind_dict[root_val]
            if root_inorder_idx > inorder_end or root_inorder_idx < inorder_start:
                return None

            root = TreeNode(preorder.pop(0))
            root.left = buildTreeNode(preorder, inorder_start, root_inorder_idx - 1)
            root.right = buildTreeNode(preorder, root_inorder_idx + 1, inorder_end)

            return root

        return buildTreeNode(preorder, 0, len(inorder) - 1)


a = Solution()
a.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
