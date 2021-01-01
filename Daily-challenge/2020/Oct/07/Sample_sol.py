# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode: 
        
        if not head: 
            return head 
        
        # find length of the list 
        n = 0 
        node = head
        while node: 
            n += 1 
            if not node.next: 
                tail = node 
            node = node.next 
        
        k = k % n 
        
        if k == 0: 
            return head 
        
        tail.next = head 
        
        node = head 
        for _ in range(n-1-k): 
            node = node.next 
            
        new_head = node.next 
        node.next = None 
        
        return new_head 
        