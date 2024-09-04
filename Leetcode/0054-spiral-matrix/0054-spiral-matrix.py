class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n, m = len(matrix), len(matrix[0])
        visited = [[0]*m for _ in range(n)]
        
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        queue = []
        queue.append((0, 0))
        visited[0][0] = 1
        be = (0, 0)
        while queue:
            a, b = queue.pop()
            ans.append(matrix[a][b])

            x = a + be[0]
            y = b + be[1]
            if x < n and x >= 0 and y < m and y >= 0 and not visited[x][y]:
                queue.append((x,y))
                visited[x][y] = 1
                continue
            for xx, yy in directions:
                x = a + xx
                y = b + yy
                
                if x < n and x >= 0 and y < m and y >= 0 and not visited[x][y]:
                    queue.append((x,y))
                    visited[x][y] = 1
                    be = (xx, yy)
                    break
                
        return ans