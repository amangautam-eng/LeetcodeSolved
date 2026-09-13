class Solution:
    def reverseWords(self, s: str) -> str:

        ans=s.strip().split()
        i,j=0,len(ans)-1
        while i<=j:
            ans[i],ans[j]=ans[j],ans[i]
            i+=1
            j-=1

        
        text=" ".join(ans)

        return text
        