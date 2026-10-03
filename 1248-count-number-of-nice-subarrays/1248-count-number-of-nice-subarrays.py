class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        
        def subarray(arr,k):
            left,odd,sub=0,0,0

            for right in range(len(arr)):
                if arr[right]%2!=0:
                    odd+=1

                while odd>k:
                    if arr[left]%2!=0:
                        odd-=1
                    left+=1

                sub+= (right-left+1)

            return sub

        
        return subarray(nums,k)-subarray(nums,k-1)



