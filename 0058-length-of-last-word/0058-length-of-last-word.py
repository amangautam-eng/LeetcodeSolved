class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        ans=s.strip().split(' ')

        return len(ans[-1])
        