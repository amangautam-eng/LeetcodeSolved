class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res=max(nums)
        currMin,currMax=1,1

        for x in nums:

            if x==0:
                currMin,currMax=1,1
                continue

            temp=x*currMax
            currMax=max(x,x*currMax,x*currMin)
            currMin=min(temp,x, x*currMin)

            res=max(res,currMin,currMax)

        return res
        