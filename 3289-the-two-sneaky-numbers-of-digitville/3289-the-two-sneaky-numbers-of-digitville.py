class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        freq=set()
        ans=[]

        for x in nums:
            if x in freq:
                ans.append(x)
            else:
                freq.add(x)

        return ans
        