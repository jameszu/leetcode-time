"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        while node:
            cur = dummy = Node(0)
            while node:
                if node.left:
                    cur.next = node.left
                    cur = cur.next
                    
                if node.right:
                    cur.next = node.right
                    cur = cur.next
                    
                node = node.next
            node = dummy.next
        return root