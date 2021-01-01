# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        temp = head
        cur = head
        count = 1
        lens = 0
        while temp != None:
            temp = temp.next
            lens += 1
        if lens == 0:
            return head
        k = k % lens
        tar = lens - k
        while count <tar and cur != None:
            cur = cur.next
            count += 1
        # print(cur)
        if cur == None:
            return 
 
        kth = cur
        while cur.next != None:
            cur = cur.next
        # print(kth,head)
        cur.next = head
        head = kth.next
        kth.next = None
        return head