"""https://leetcode.com/problems/
binary-search-tree-iterator/submissions/1477270991"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.pointer = TreeNode(-1)
        self.inorder_arr = []

        def inorder(cur: Optional[TreeNode]):
            if cur == None:
                return

            inorder(cur.left)
            self.inorder_arr.append(cur)
            inorder(cur.right)

        inorder(root)

        self.next_ind = 0

    def next(self) -> int:
        self.pointer = self.inorder_arr[self.next_ind]
        self.next_ind += 1
        return self.pointer.val

    def hasNext(self) -> bool:
        return self.next_ind < len(self.inorder_arr)


a = BSTIterator(TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20))))

print(a.next(), a.next(), a.next())
