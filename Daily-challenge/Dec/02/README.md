# Linked List Random Node
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom(); <br>

## Idea
two ways, one is to use a list and cheat, or we can use standard while loop and extra space for the dummy nodes and etc.
## Code
```python
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
        
```