class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        ans=[]

        sort=sorted(numbers)
        left,right=0,len(sort)-1

        while left<right:

            if sort[left]+sort[right] == target:
                ans=[left+1,right+1]
                return ans

            elif sort[left]+sort[right] < target:
                left+=1
            
            elif sort[left]+sort[right] > target:
                right-=1

            else:
                pass

        
        return ans
        