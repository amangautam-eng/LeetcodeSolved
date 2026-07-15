class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        s = 0
        avg = float("-inf")

        for r in range(len(nums)):
            s += nums[r]
            if r - l + 1 > k:
                s -= nums[l]
                l += 1
            if r - l + 1 == k:
                avg = max(avg, s / k)

        return avg
