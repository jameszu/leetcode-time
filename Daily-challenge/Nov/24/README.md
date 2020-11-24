# Basic Calculator II
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.<br>

## Idea
Just do while loop and convert to decimal

## Code
```python
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
        
```