# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while(slow is not None and fast is not None):
            if slow == fast:
                return True
            
            slow = slow.next
            count = 0
            while(fast is not None and count < 2):
                fast = fast.next
                count+=1

        
        return False