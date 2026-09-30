# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        curr1 = list1
        curr2 = list2
        newHead = list1 if list1.val <= list2.val else list2
        newCurr = None
        while curr1 and curr2:
            num1 = curr1.val
            num2 = curr2.val
            if num1 <= num2:
                newCurr = curr1
                curr1 = curr1.next
                newCurr.next = curr2
            else:
                newCurr = curr2
                curr2 = curr2.next
                newCurr.next = curr1

        return newHead