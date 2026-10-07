class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        arr=[0]
        curr=0

        for x in gain:
            curr+=x
            arr.append(curr)

        return max(arr)
        