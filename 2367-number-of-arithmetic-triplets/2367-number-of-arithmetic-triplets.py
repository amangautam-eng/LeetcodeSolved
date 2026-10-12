class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:

        count=0
        freq=set(nums)

        for x in nums:
            if (x+diff) in freq and (x+2*diff) in freq:
                count+=1

        return count
