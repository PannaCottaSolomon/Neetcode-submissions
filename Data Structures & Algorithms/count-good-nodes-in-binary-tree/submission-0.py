# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def bfs(root):
            if not root:
                return

            nonlocal ans
            prevHighest = root.val
            queue = deque([(root, prevHighest)])

            while queue:
                n = len(queue)
                for _ in range(n):
                    curr, prevHighest = queue.popleft()
                    if prevHighest <= curr.val:
                        ans += 1

                    prevHighest = max(curr.val, prevHighest)
                    if curr.left:
                        queue.append((curr.left, prevHighest))
                    if curr.right:
                        queue.append((curr.right, prevHighest))


        bfs(root)
        return ans