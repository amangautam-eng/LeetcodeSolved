class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        
        for i, num in enumerate(nums):
            # If duplicate is found within the last k elements
            if num in window:
                return True
                
            # Add current number to the window
            window.add(num)
            
            # Maintain the window size of k
            if len(window) > k:
                window.remove(nums[i - k])
                
        return False