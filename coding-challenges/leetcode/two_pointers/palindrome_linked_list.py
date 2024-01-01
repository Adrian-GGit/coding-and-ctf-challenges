# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow_next = slow.next
            slow.next = prev
            prev = slow
            slow = slow_next

        if fast:
            slow = slow.next

        while prev:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True