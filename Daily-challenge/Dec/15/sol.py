# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        global res
        res = 0
        
        def tran(root):
            global res
            if root == None: return
            # print(root.val)
            if low <= root.val <= high:
                res += root.val
            if low < root.val:
                tran(root.left)
            if root.val < high:
                tran(root.right)
        tran(root)
        return res