# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True

        def dfs(root):
            if not root:
                return

            nonlocal isValid

            currVal = root.val
            if root.left:
                leftChild = root.left
                leftVal = leftChild.val
                if leftVal >= currVal:
                    isValid = False
                dfs(leftChild)
            if root.right:
                rightChild = root.right
                rightVal = rightChild.val
                if currVal >= rightVal:
                    isValid = False
                dfs(rightChild)

        dfs(root)
        return isValid