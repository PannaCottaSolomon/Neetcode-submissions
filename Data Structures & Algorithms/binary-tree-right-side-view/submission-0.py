# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def bfs(root):
            nonlocal ans

            visited = set()
            queue = deque([root])

            while queue:
                numNodes = len(queue)
                for i in range(numNodes):
                    curr = queue.popleft()
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right) 

                    if i == numNodes - 1:
                        ans.append(curr.val)

            return

        bfs(root)
        return ans