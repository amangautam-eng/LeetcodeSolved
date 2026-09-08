class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l=0
        minlen=float('inf')
        s=0

        for r in range(0,len(nums)):
            s+=nums[r]

            while(s>=target):

                minlen=min(minlen, r-l+1)
                s-=nums[l]
                l+=1

        return minlen if minlen != float('inf') else  0
