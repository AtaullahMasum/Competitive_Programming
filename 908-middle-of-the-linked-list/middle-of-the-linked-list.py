# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        count = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 2
        if fast is None:
            count -= 1
        if count % 2==0:
            return slow.next
        else:
            return slow
        