class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans=[]
        for x in range(m):
            if x==m-1:
                ans.append("."*n)
            else:
                st=""
                for y in range(n):
                    
                    if y==0:
                        st+="."
                    else:
                        st+="#"
                print(st)
                ans.append(st)

        return ans

        