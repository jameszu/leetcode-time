# Insertion Sort List


Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5 <br>

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