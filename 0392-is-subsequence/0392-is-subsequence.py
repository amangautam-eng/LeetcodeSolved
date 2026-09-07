class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left, right = 0, 0
        
        # Move through both strings safely
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1  # Only move s pointer on a match
            right += 1     # Always move t pointer
            
        # If left reached the end, all characters in s were found in t
        return left == len(s)
