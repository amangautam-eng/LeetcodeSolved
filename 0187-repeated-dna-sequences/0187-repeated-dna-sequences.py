class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        ans=[]
        if len(s)<10:
            return ans

        freq={}
        

        left,right=0,10

        while right<=len(s):
            curr=s[left:right]

            freq[curr]=1+freq.get(curr,0)

            left+=1
            right+=1

        for item in freq:
            if freq[item]>1:
                ans.append(item)
        return ans

        



        