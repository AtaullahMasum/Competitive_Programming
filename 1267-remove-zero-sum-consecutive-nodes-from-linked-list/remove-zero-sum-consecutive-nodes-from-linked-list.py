# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_sum = {0: ListNode(0)}  # Store prefix sum and the corresponding node
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        prefix_sum_val = 0

        while current:
            prefix_sum_val += current.val
            prefix_sum[prefix_sum_val] = current
            current = current.next

        current = dummy
        prefix_sum_val = 0

        while current:
            prefix_sum_val += current.val
            current.next = prefix_sum[prefix_sum_val].next
            current = current.next

        return dummy.next
        