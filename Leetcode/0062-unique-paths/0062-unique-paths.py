class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = [[0]*n for _ in range(m)]
        
        def findRoute(a, b):
            if b == n:
                return
            
            if a >= 0 and a < m and b >= 0 and b < n:
                if a - 1 < 0 or b - 1 < 0:
                    visited[a][b] = 1
                else:
                    visited[a][b] = visited[a-1][b] + visited[a][b-1]
                findRoute(a, b + 1)
        for i in range(m):
            findRoute(i, 0)
        
        return visited[m-1][n-1]