class Solution:
    def longestOnes(self, nums: List[int], k: int):
        l = 0
        zerocnt = 0
        maxlen = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zerocnt += 1

            while zerocnt > k:
                if nums[l] == 0:
                    zerocnt -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)

        return maxlen