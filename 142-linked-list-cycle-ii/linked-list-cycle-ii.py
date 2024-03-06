# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
       # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return None
        
        # Initialize slow and fast pointers
        slow = head
        fast = head
        
        # Move slow and fast pointers until they meet inside the cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If slow and fast pointers meet, it indicates the presence of a cycle
            if slow == fast:
                break
        else:
            return None  # No cycle found
        
        # Move slow pointer back to the head
        slow = head
        
        # Move slow and fast pointers until they meet at the start of the cycle
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Return the node where the cycle starts
        return slow
        