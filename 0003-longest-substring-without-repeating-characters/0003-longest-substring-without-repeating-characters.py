class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left,right=0,0

        char=set()
        maxlen=0

        while right<len(s):

            while s[right] in char:
                char.remove(s[left])
                left+=1

            
            char.add(s[right])
            right+=1

            maxlen=max(maxlen,right-left)

        return maxlen