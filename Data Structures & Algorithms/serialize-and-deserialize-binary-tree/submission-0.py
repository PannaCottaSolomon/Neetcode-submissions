# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        def bfs(root):
            if not root:
                return

            res = []
            queue = collections.deque([root])
            # print(root.val)
            while queue:
                n = len(queue)
                for _ in range(n):
                    curr = queue.popleft()
                    res.append(str(curr.val))
                    
                    if curr.left:
                        queue.append(curr.left)
                    else:
                        res.append("null")
                    if curr.right:
                        queue.append(curr.right)
                    else:
                        res.append("null")

            return res

        res = bfs(root)
        print(res)
        return "#".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return

        nodes = data.split("#")
        # print(nodes)
        def createTree(nodes):
            if len(nodes) == 0:
                return

            rootVal = int(nodes[0])
            newRoot = TreeNode(rootVal)
            queue = collections.deque()
            queue.append(newRoot)

            i = 1
            while i < len(nodes):
                listVal = nodes[i]
                curr = queue.popleft()

                if not curr.left and listVal != "null":
                    curr.left = TreeNode(int(listVal))  
                elif listVal == "null":
                    curr.left = None
                else:
                    curr.right = TreeNode(int(listVal))

                queue.append(curr.left)
                queue.append(curr.right) 
                i += 1

            return newRoot    
        
        newRoot = createTree(nodes)
        return newRoot








