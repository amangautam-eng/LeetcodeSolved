class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        currmax=nums[0]
        globalmax=nums[0]

        for i in range(1,len(nums)):

            currmax=max(nums[i],nums[i]+currmax)
            globalmax=max(currmax,globalmax)

        return globalmax

        