class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        freq={}

        for i in range(len(s)):

            if s[i] in freq:
                if freq[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in freq.values():
                    return False
                freq[s[i]]=t[i]

        return True
                
        