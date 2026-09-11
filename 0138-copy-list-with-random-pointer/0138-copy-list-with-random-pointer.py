"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr=head
        freq={None:None}
        while curr:
            newnode=Node(curr.val)

            freq[curr]=newnode

            curr=curr.next

        head2=freq[head]
        curr=head

        while curr:
            freq[curr].next=freq[curr.next]
            freq[curr].random=freq[curr.random]
            curr=curr.next

        return head2