# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        rootNode = preorder[0]
        idxRoot = inorder.index(rootNode)
        leftTree = inorder[:idxRoot]
        rightTree = inorder[idxRoot + 1:]

        root = TreeNode(rootNode)
        curr = root
        
        i = len(leftTree)
        while i > 0:
            curr.left = TreeNode(leftTree[-i])
            i -= 1
            curr = curr.left
        
        curr = root
        j = 0
        while j < len(rightTree):
            curr.right = TreeNode(rightTree[j])
            j += 1
            curr = curr.right

        return root


