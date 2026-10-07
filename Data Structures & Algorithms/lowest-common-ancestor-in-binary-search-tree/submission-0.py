# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return

        lca = root
        def dfs(root, p, q):
            curr = root.val
            lca = root
            if p.val > curr and q.val > curr:
                lca = dfs(root.right, p, q)
            elif p.val < curr and q.val < curr:
                lca = dfs(root.left, p, q)
            # print(lca.val)
            return lca
        
        lca = dfs(root, p, q)
        return lca