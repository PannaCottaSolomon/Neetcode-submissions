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
            leftMaxes = [0, 0]
            rightMaxes = [0, 0]
            if root.left:
                leftMaxes = dfs(root.left)
            if root.right:
                rightMaxes = dfs(root.right)

            curr = root.val
            localMax = [max(curr, curr + leftMaxes[0], curr + rightMaxes[0]), curr + leftMaxes[0] + rightMaxes[0]]

            highest = max(highest, localMax[0], localMax[1])
            # print(localMax)
            return localMax 

        dfs(root)
        return highest