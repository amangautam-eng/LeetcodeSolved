# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head==None or head.next==None or k==0:
            return head

        size=0
        curr=head
        while curr:
            size+=1
            curr=curr.next

        k=k%size
        left=head
        right=head

        for _ in range(k):
            right=right.next

        while right.next:
            right=right.next
            left=left.next

        right.next=head
        head2=left.next
        left.next=None
        print(head2.val)
        return head2


        