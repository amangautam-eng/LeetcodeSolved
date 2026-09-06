class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        cnt=0
        ans=[0]*len(nums)

        for i in range(len(nums)):
            if nums[i]==0:
                cnt+=1
            else:
                product*=nums[i]

            if cnt>1:
                return ans

        for i in range(len(nums)):
            if cnt==1:
                if nums[i]==0:
                    ans[i]=product

            else:
                ans[i]=int(product/nums[i])
            
        return ans

        
        