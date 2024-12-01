# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.slow_p = self.fast_p = head
        self.prev = None

        while self.fast_p and self.fast_p.next:
            self.prev = self.slow_p # store this to later remove the mid element
            self.slow_p = self.slow_p.next
            self.fast_p = self.fast_p.next.next

        if self.prev:
            self.prev.next = self.slow_p.next
        else:
            return None

        return head
        