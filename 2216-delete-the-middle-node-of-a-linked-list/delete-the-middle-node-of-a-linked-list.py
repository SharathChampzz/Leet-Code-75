# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            This can be solved using the slow and fast pointer technique because the middle element can be identified using this method.
            The logic is that if you move the fast pointer two steps and the slow pointer one step, the fast pointer will reach the end first.
            At that exact time, the slow pointer will be pointing to the middle of the list.
        """
        if not head or not head.next:
            return None

        self.slow_p = self.fast_p = head
        self.prev = None

        while self.fast_p and self.fast_p.next:
            self.prev = self.slow_p # store this to later remove the mid element
            self.slow_p = self.slow_p.next
            self.fast_p = self.fast_p.next.next

        self.prev.next = self.slow_p.next

        return head
        