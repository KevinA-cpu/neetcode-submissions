# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer =[]
        cur=head
        prev=None
        isFirst=True
        while(cur):
            if prev:
                temp=cur.next
                if isFirst:
                    prev.next=None
                    isFirst=False
                cur.next=prev
                prev=cur
                cur=temp
            else:
                prev=cur
                cur=cur.next
        head=prev
        return head