# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return

        length = 0
        l1 = head.next
        l2 = head
        while(l2 is not None):
            l2 = l2.next
            length+=1
        
        half = math.ceil((length - 1) / 2)
        count = 1

        l4 = head
        l2 = head.next
        while(count < half):
            l2 = l2.next
            l4 = l4.next
            count+=1
        
        # Reverse
        l3 = l2.next
        l2.next = None
        l4.next = None
        while(l3 is not None):
            temp = l3.next
            l3.next = l2
            l2 = l3
            l3 = temp
       
        head.next = l2
        while(l2 is not None and l1 is not None and l1 is not l2):
            temp = l2.next
            l2.next = l1
            l2 = l1
            l1 = temp
