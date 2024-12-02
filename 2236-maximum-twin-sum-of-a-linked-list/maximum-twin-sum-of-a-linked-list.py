# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
            Two-Pointer Technique: Uses slow and fast pointers to find the middle of the list.

            Reverse the Second Half: Reverses the second half of the list.

            Calculate Twin Sums: Iterates through the first half and the reversed second half to calculate the twin sums.
        """
        # Step 1: Find middle element using slow and fast pointer
        slow_p = fast_p = head

        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        # Step 2: Reverse the rest of the list, So that we can take sum of first and second list together
        prev, curr = None, slow_p
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Step 3: Take sum of first and second list now
        first, second = head, prev
        result = float('-inf')

        while first and second:
            result = max(result, first.val + second.val)       
            first = first.next
            second = second.next

        return result

    def pairSumSameTimeButMoreSpaceComplexity(self, head: Optional[ListNode]) -> int:
        """
        Logic:
            Two-Pointer Technique: Uses slow and fast pointers to find the middle of the list.

            List to Store Values: Stores the values of the first half of the list in a list (sums).

            Calculate Twin Sums: Iterates through the second half of the list, updating the sums list and calculating the twin sums.

            Time Complexity: O(n)
            Space Complexity: O(n/2)
        """
        slow_p = fast_p = head
        sums = []

        while fast_p and fast_p.next:
            sums.append(slow_p.val)
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        index = len(sums) - 1
        result = float('-inf')

        while slow_p:
            sums[index] += slow_p.val
            result = max(result, sums[index])
            index -= 1
            slow_p = slow_p.next

        return result
