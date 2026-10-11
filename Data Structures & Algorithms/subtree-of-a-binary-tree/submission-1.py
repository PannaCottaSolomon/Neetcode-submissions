# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tree = []
        subTree = []

        def dfs(root, tree):
            if not root:
                return

            tree.append(str(root.val))
            if root.left:
                dfs(root.left, tree)
            else:
                tree.append("null")
            if root.right:
                dfs(root.right, tree)
            else:
                tree.append("null")
            
            return tree

        tree = dfs(root, tree)
        subTree = dfs(subRoot, subTree)
        # print(tree)
        # print(subTree)

        treeString = "".join(tree)
        subTreeString = "".join(subTree)
        # print(treeString, subTreeString)
        if subTreeString in treeString:
            return True
        return False

