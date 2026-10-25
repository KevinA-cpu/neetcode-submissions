# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        l1 = head
        while(l1 is not None):
            l1 = l1.next
            length+=1
        
        length = length - n
        count = 0
        print(length)
        l1, l2 = None, head
        while (count < length):
            l1 = l2
            l2 = l2.next
            count+=1
        
        if l1 is None:
            try:
                head = head.next
            except:
                head = None
        else:
            l1.next = l2.next
        return head