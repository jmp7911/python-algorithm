class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        visited = [[0]*n for _ in range(m)]
        def findRoute(a, b):
            if b == n:
                return
            
            if a >= 0 and a < m and b >= 0 and b < n and not obstacleGrid[a][b]:
                if a - 1 < 0 and b - 1 < 0:
                    visited[a][b] = 1 if not obstacleGrid[a][b] else 0
                elif a - 1 < 0:
                    visited[a][b] = visited[a][b-1]
                elif b - 1 < 0:
                    visited[a][b] = visited[a-1][b]
                else:
                    visited[a][b] = visited[a-1][b] + visited[a][b-1]
            findRoute(a, b + 1)
        for i in range(m):
            findRoute(i, 0)
        
        return visited[m-1][n-1]