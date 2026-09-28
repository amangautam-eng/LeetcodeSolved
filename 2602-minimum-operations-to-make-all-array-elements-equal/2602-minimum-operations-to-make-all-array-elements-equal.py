from bisect import bisect_left
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:

        n=len(nums)
        nums.sort()
        prefix=[0]
        ans=[]
        total=0
        for x in nums:
            total+=x
            prefix.append(total)

        for q in queries:

            idx=bisect_left(nums,q)

            left= q*(idx) - prefix[idx]

            right= (prefix[-1]-prefix[idx]) - (n-idx)*q

            ans.append(left+right)

        return ans

        
        
        
        