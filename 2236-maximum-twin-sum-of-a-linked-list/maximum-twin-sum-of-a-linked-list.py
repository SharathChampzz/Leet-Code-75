# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow_p = fast_p = head
        sums = []

        while fast_p:
            sums.append(slow_p.val)
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        index = len(sums) - 1
        result = float('-inf')

        try:
            while slow_p:
                sums[index] += slow_p.val
                result = max(result, sums[index])
                index -= 1
                slow_p = slow_p.next
        except Exception as err:
            print(err)

        return result

        