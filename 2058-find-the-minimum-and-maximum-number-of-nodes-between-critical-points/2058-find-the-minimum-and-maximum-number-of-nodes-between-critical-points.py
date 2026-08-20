# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        minlen,maxlen=float('inf'),0

        prev=head
        curr=head.next
        count=1
        ind=[]

        while curr and curr.next:
            count+=1
            is_max = curr.val > prev.val and curr.val > curr.next.val
            is_min = curr.val < prev.val and curr.val < curr.next.val
    
            if is_max or is_min:
                ind.append(count)

            prev=curr
            curr=curr.next

        if len(ind)<2:
            return [-1,-1]

        for i in range(1,len(ind)):

            minlen=min(minlen,ind[i]-ind[i-1])

        maxlen = ind[-1] - ind[0]

        return [minlen,maxlen]




        
        

        