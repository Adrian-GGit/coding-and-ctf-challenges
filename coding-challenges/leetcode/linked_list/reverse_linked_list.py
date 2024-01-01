# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rev_list(head, None)

    def rev_list(self, head, before):
        if head:
            original_head_next = head.next
            head.next = before
            return self.rev_list(original_head_next, head)
        return before