class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Using set(nums) is faster and automatically removes duplicates
        empty = set(nums)

        maxlen = 0
        
        # 2. Iterate over the SET to avoid checking duplicate elements
        for x in empty:
            # 3. Check if 'x' is the absolute START of a sequence
            if x - 1 not in empty:
                cnt = 0
                temp = x
                # 4. Count forward from the start
                while temp in empty:
                    temp += 1
                    cnt += 1
                maxlen = max(maxlen, cnt)

        return maxlen
