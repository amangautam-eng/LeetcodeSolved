class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def f(i,nums,arr,temp):

            if i>=len(nums):

                arr.append(list(temp))
                return

            temp.append(nums[i])
            f(i+1,nums,arr,temp)

            temp.remove(nums[i])

            f(i+1,nums,arr,temp)

            return arr
        
        arr=[]
        temp=[]
        return f(0,nums,arr,temp) 

        