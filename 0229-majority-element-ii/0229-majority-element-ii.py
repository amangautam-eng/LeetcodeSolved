class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:

        ans=[]
        freq={}

        for x in nums:
            freq[x]=1+freq.get(x,0)

        for x in freq:
            if freq[x]>len(nums)/3:
                ans.append(x)

        return ans
        