class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        running=[]
        i=0
        for x in nums:
            running.append(x+i)
            i+=x

        return running


        