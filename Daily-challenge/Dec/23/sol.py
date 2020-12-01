# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def helper(node):
            if not node: 
                return (0, 0)
            l1, l2 = helper(node.left)
            r1, r2 = helper(node.right)
            
            return (node.val + l2 + r2, max(l1, l2) + max(r1, r2))
            
            
        return max(helper(root))
        