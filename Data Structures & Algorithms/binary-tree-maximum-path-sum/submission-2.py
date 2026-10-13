# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        highest = -1001

        def dfs(root):
            if not root:
                return

            nonlocal highest
            left = 0
            right = 0
            if root.left:
                leftMaxes = dfs(root.left)                
                left = max(leftMaxes)
            if root.right:
                rightMaxes = dfs(root.right)
                right = max(rightMaxes)

            curr = root.val

            localMax = [max(curr, curr + left, curr + right), curr + left + right]

            highest = max(highest, localMax[0], localMax[1])
            # print(localMax)
            return localMax 

        dfs(root)
        return highest