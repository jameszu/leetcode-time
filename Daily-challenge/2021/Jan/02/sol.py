# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or not cloned:
            return None
        stack = []
        stack += [(original,cloned)]
        while stack:
            org, clone = stack.pop()
            
            if org == target:    
                return clone
            if org.left:
                stack.append((org.left, clone.left))
            if org.right:
                stack.append((org.right, clone.right))