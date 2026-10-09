class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        sort=sorted(nums)
        left,right=0,len(sort)-1
        ans=0
        while left<right:
            total=sort[left]+sort[right]
            ans=max(total,ans)

            left+=1
            right-=1

        return ans


        