class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        freq={}

        for i,x in enumerate(nums):
            if x in freq and abs(i-freq[x])<=k:
                return True

            else:
                freq[x]=i

        return False
