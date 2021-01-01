class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        moves = [(1,-1),(1,0),(1,1)]
        m,n = len(grid), len(grid[0])
        @functools.lru_cache(None)
        def dp(r1,c1,r2,c2):
            if(c1>c2): return dp(r2,c2,r1,c1)
            if not (r1<m and r2<m and 0<=c1<n and 0<=c2<n):
                return float("-inf")
            if r1==m-1:
                return grid[r1][c1]+grid[r2][c2] if r1!=r2 or c1!=c2 else 0
            maxi = 0
            for d1 in moves:
                for d2 in moves:
                    dr1,dc1=r1+d1[0],c1+d1[1]
                    dr2,dc2=r2+d2[0],c2+d2[1]
                    maxi = max(maxi, dp(dr1,dc1,dr2,dc2)+grid[r1][c1]+grid[r2][c2] if r1!=r2 or c1!=c2 else 0)
            return maxi
        return dp(0,0,0,n-1)