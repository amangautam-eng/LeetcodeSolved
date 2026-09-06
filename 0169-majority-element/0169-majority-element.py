class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq={}

        for x in nums:
            freq[x]=1+freq.get(x,0)

        for x in freq:
            if freq[x]>int(len(nums)/2):
                return x

