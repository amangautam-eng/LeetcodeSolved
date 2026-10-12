class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        freq=set()

        for x in nums:
            if x in freq:
                return True
            else:
                freq.add(x)

        return False
        