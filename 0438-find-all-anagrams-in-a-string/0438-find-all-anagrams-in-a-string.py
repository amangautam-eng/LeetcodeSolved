class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        freq_s={}
        freq_p={}
        ans=[]
        for c in p:
            freq_p[c]=1+freq_p.get(c,0)

        for right in range(len(p)):
            freq_s[s[right]]=1+freq_s.get(s[right],0)

        if freq_s==freq_p:
            ans.append(0)
        left=0

        for right in range(len(p),len(s)):
            
            freq_s[s[right]]=1+freq_s.get(s[right],0)
            freq_s[s[left]]-=1

            if freq_s[s[left]]==0:
                del freq_s[s[left]]

            left+=1

            if freq_s==freq_p:
                ans.append(left)

        return ans




        