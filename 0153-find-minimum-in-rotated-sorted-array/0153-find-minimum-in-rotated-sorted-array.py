class Solution:
    def findMin(self, nums: list[int]) -> int:
        sort=sorted(nums)

        return sort[0]