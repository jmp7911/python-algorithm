class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = [False]
        m = len(board[0])
        n = len(board)
        visited = [[0 for _ in range(m)] for _ in range(n)]
        
        def bfs(x, y, i):
            # print(x, y, i)
            if i == len(word):
                ans[0] = True
                return
            directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
            for xx, yy in directions:
                a, b = x + xx, y + yy
                if a >= 0 and a < n and b >= 0 and b < m:
                    if visited[a][b] == 0 and board[a][b] == word[i]:
                        visited[a][b] = 1
                        i += 1
                        bfs(a, b, i)
                        visited[a][b] = 0
                        i -= 1
        for x in range(n):
            for y in range(m):
                if board[x][y] == word[0]:
                    visited[x][y] = 1
                    bfs(x, y, 1)
                    visited[x][y] = 0
        
        return ans[0]