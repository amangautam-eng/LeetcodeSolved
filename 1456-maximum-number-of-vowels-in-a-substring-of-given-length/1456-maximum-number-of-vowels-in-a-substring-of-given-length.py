class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowcount=0
        maxvowel=0

        left,right=0,0

        vow={'a','e','i','o','u'}
        while right-left<k:
            if s[right] in vow:
                vowcount+=1
            right+=1

        maxvowel=vowcount

        while right<len(s):
            if s[right] in vow:
                vowcount+=1

            if s[left] in vow:
                vowcount-=1

            right+=1
            left+=1
            maxvowel=max(maxvowel,vowcount)

        return maxvowel

