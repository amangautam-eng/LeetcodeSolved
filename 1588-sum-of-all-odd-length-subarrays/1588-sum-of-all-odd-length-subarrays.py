class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total = 0
        n = len(arr)
        
        for i in range(n):
            # Calculate how many total subarrays include arr[i]
            total_subarrays = (i + 1) * (n - i)
            # Find the number of odd-length subarrays
            odd_subarrays = (total_subarrays + 1) // 2
            
            total += odd_subarrays * arr[i]
            
        return total



            

            

        