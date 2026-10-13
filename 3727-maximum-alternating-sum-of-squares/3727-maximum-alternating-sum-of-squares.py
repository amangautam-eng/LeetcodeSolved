class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        temp=[]
        for x in nums:
            temp.append(abs(x))

        temp=sorted(temp)
        left=0
        right=len(temp)-1
        total=0

        while left<right:
            total+= temp[right]**2
            total-= temp[left]**2

            right-=1
            left+=1
        if len(temp)%2!=0:
            total+= temp[right]**2
        return total
        