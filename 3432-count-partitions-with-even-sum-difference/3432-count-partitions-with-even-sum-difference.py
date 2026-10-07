class Solution:
    def countPartitions(self, nums: List[int]) -> int:

        running=[]
        total,curr,ans=sum(nums),0,0
        for x in nums:
            curr+=x
            running.append(curr)

        for i in range(len(nums)-1):

            if abs((total-running[i])-running[i])%2==0:
                ans+=1

        return ans

        

            
        