# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.get_linked_list(l1, l2)

    def get_linked_list(self, l1, l2, c=0):
        linked_list = ListNode()
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        new_val = l1_val + l2_val + c
        carry = 1 if new_val > 9 else 0
        new_val -= 10 if new_val > 9 else 0
        linked_list.val = new_val
        l1 = l1.next if l1 is not None else l1
        l2 = l2.next if l2 is not None else l2
        if l1 or l2 or carry:
            linked_list.next = self.get_linked_list(l1, l2, carry)
        return linked_list