from collections import deque
def solution(maps):
    count = 0
    queue = deque()
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))] 
    directions = ((0, -1), (-1, 0), (1, 0), (0,1))
    queue.append((0,0))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for xx, yy in directions:
            _x = x + xx
            _y = y + yy
            if _x >= 0 and _x < len(maps) and _y >= 0 and _y < len(maps[0]):
                if maps[_x][_y] and visited[_x][_y] < 0:
                    visited[_x][_y] = visited[x][y]+1
                    queue.append((_x, _y))
    
    # print(visited)
    return visited[len(maps)-1][len(maps[0])-1]
    