# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        it = self.isValidBST(root)
        a, b = next(it)
        c = next(it, None)
        if c:
            _, c = c
            a.val, c.val = c.val, a.val
        else:
            a.val, b.val = b.val, a.val
        return root

    def isValidBST(self, root):
        pre, cur, stack = None, root, []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            s = stack.pop()
            if pre and s.val <= pre.val:
                yield pre, s
            pre, cur = s, s.right
        