# Rotate List
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

---
## Idea
Its a different version of the G4G one. This question is like imagine the list is in a fixed position. <br>
The overflow value will go back. <br>
My algorithm is to determine the last value of the linked list with given k. Then append the head list onto the front. <br>

## Code
```python
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
```
