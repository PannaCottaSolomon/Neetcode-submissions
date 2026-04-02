# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        left = None
        curr = head
        right = head.next
        curr.next = left

        while right is not None:
            left = curr
            curr = right
            right = right.next
            curr.next = left

        newHead = curr
        return newHead
