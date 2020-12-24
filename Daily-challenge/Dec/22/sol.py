# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            lefth, leftb = dfs(root.left)
            righth, rightb = dfs(root.right)
            return max(lefth, righth) + 1, abs(lefth - righth) <= 1 and leftb and rightb
        
        return dfs(root)[1]