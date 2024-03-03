# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
       
        prev = None
        current = head
        while current :
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
        