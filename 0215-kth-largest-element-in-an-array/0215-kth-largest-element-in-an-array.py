import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxheap = []

        for x in nums:
            heapq.heappush(maxheap, -x)

        for _ in range(k - 1):
            heapq.heappop(maxheap)

        return -heapq.heappop(maxheap)