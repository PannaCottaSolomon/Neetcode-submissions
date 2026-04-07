# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        if curr is None:
            return
            
        if curr.left and curr.right:
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
        elif not curr.left and curr.right:
            curr.left = curr.right
            curr.right = None
        elif not curr.right and curr.left:
            curr.right = curr.left
            curr.left = None
        else:
            return root

        self.invertTree(curr.left)
        self.invertTree(curr.right)

        print(curr.val)
        return root