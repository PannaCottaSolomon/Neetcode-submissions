# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def bfs(root):
            if not root:
                return 

            visited = set()
            queue = deque([root])
            while queue:
                level = []
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    visited.add(curr)

                    level.append(curr.val)

                    if curr.left and curr.left not in visited:
                        queue.append(curr.left)
                    if curr.right and curr.left not in visited:
                        queue.append(curr.right)
                
                ans.append(level)

            return

        bfs(root)
        return ans