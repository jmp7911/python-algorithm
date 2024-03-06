
import sys
N, M = map(int, sys.stdin.readline().split())

def backtracking(n, r, result, visited):
    if not r:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        if not visited[i] and (not result or result[-1] < i):
            visited[i] = True
            result.append(i)
            backtracking(n, r-1, result, visited)
            visited[i] = False
            result.pop()
visited = [False]*(N+1)
backtracking(N, M, [], visited)