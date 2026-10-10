# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []

        def dfs(root, tree):
            if not root:
                return

            curr = root.val
            tree.append(curr)
            tree1 = dfs(root.left, tree) if root.left else [None]
            tree2 = dfs(root.right, tree) if root.right else [None]
            
            return tree + tree1 + tree2

        tree1 = dfs(p, tree1)
        tree2 = dfs(q, tree2)
        return tree1 == tree2