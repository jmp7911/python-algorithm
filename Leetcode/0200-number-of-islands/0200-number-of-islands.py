class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dics = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])

        visited = [[0] * n for _ in range(m)]
        queue = []
        result = 0

        for i in range(m):
            for j in range(n):
                print(i, j)
                if not visited[i][j] and grid[i][j] == "1":
                    queue.append((i, j))
                    
                    result += 1
                while queue:
                    x, y = queue.pop()
                    visited[x][y] = 1
                    
                    for dx, dy in dics:
                        xx = x + dx
                        yy = y + dy

                        if xx < m and xx >= 0 and yy < n and yy >= 0 and not visited[xx][yy] and grid[xx][yy] == "1":
                            queue.append((xx, yy))
                            
                
        
        return result