# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        mylist=[]
        ptr=head
        while ptr:
            mylist.append(ptr.val)
            ptr=ptr.next
            
        mylist.sort()
        
        ptr=head
        for val in mylist:
            ptr.val=val
            ptr=ptr.next
            
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dum = ListNode(0)
        prev = dum
        
        while head:
            temp = head.next
            if prev.val >= head.val:
                prev = dum
            while prev.next and prev.next.val < head.val:
                prev = prev.next
                
            head.next = prev.next
            prev.next = head
            head = temp
        return dum.next
        