class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i,x in enumerate(nums):

            digitsum=0
            for c in str(x):
                digitsum+=int(c)

            if digitsum==i:
                return i

        return -1


        