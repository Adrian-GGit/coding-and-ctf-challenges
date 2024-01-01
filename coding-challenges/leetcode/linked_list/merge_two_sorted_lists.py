# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1
        head, list1, list2 = self.get_current(list1, list2)
        current = head
        while list1 or list2:
            current.next, list1, list2 = self.get_current(list1, list2)
            current = current.next
        return head

    def get_current(self, list1, list2):
        if not list1 and not list2:
            return (None, None, None)
        elif not list2:
            return (list1, list1.next, None)
        elif not list1:
            return (list2, None, list2.next)
        return (list1, list1.next, list2) if list1.val <= list2.val else (list2, list1, list2.next)