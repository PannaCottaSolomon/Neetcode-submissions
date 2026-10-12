# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True
        INF = 10 ** 18
        limits = [-INF, INF]

        def dfs(root, limits):
            if not root:
                return

            nonlocal isValid

            currVal = root.val
            if not limits[0] < currVal < limits[1]:
                isValid = False

            if root.left:
                dfs(root.left, [limits[0], currVal])
            if root.right:
                dfs(root.right, [currVal, limits[1]])

        dfs(root, limits)
        return isValid