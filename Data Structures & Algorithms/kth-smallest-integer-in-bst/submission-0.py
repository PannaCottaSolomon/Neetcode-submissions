# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        num = root.val

        def dfs(root, k):
            if not root:
                return
            
            nonlocal num
            nonlocal counter

            if root.left:
                dfs(root.left, k)

            curr = root.val
            counter += 1
            if counter == k:
                num = curr

            if root.right:
                dfs(root.right, k)

            

        dfs(root, k)
        return num