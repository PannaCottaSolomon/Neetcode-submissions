# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None
        curr = head
        if curr == None:
            return curr
        while curr.next:
            right = curr.next
            curr.next = left
            left = curr
            curr = right
        curr.next = left
        return curr
