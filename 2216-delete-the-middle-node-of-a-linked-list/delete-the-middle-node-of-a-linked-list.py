# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_slow = dummy
        slow = dummy
        fast = dummy
        count = 0
        while fast and fast.next:
            
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
            count += 2
        if fast is None:
            count -=1
        if count % 2== 0:
            slow.next = slow.next.next
        else:
            prev_slow.next = slow.next
        return dummy.next

        
        