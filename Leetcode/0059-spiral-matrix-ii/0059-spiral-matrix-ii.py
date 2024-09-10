class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        visited = [[0]*n for _ in range(n)]
        
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        queue = []
        queue.append((0, 0))
        order = 1
        visited[0][0] = order
        be = None
        while queue:
            x, y = queue.pop()

            if be:
                a = x + be[0]
                b = y + be[1] 
                if a >= 0 and a < n and b >= 0 and b < n and not visited[a][b]:
                    order += 1
                    visited[a][b] = order
                    queue.append((a, b))
                    continue
                    
            for xx, yy in dirs:
                a = x + xx
                b = y + yy

                if a >= 0 and a < n and b >= 0 and b < n and not visited[a][b]:
                    order += 1
                    visited[a][b] = order
                    queue.append((a, b))
                    be = (xx, yy)
                    break

        return visited