"""https://leetcode.com/problems/
populating-next-right-pointers-in-each-node-ii/
submissions/1477255694"""

from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None

        queue = deque()
        queue.append(root)
        temp = Node(-999)

        while queue:
            prev = temp
            for i in range(len(queue)):
                popped = queue.popleft()
                if popped.left:
                    queue.append(popped.left)
                    prev.next = popped.left
                    prev = prev.next
                if popped.right:
                    queue.append(popped.right)
                    prev.next = popped.right
                    prev = prev.next

        return root
