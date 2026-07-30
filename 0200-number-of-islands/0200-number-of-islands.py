class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        r,c=len(grid),len(grid[0])

        vis=[["0" for _ in range(c)] for _ in range(r)]
        island=0

        def dfs(i,j):
            if i < 0 or i >= r or j < 0 or j >= c:
                return
            if grid[i][j]=="0" or vis[i][j]=="1":
                return

            vis[i][j]="1"

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)


        
            

        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1" and vis[i][j]=="0":
                    dfs(i,j)
                    island+=1

        return island

        


        