# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.even_head_node = self.temp_even = ListNode()
        self.odd_head_node = self.temp_odd = ListNode()

        index = 1
        while head:
            if index % 2 == 0:
                self.temp_even.next = head
                self.temp_even = head
            else:
                self.temp_odd.next = head
                self.temp_odd = head

            head = head.next
            index += 1

        self.temp_odd.next = self.even_head_node.next
        self.temp_even.next = None

        return self.odd_head_node.next

        
        