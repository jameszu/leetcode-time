# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        val = []
        def encode(node):
            if node:
                val.append(str(node.val))
                encode(node.left)
                encode(node.right)
            else:
                val.append('#')
        encode(root)
        
        return ' '.join(val)
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def decode(vals):
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = decode(vals)
            node.right = decode(vals)
            return node
        
        vals = iter(data.split())
        return decode(vals)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans