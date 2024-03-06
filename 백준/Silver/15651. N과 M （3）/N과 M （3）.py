import sys
N, M = map(int, sys.stdin.readline().split())

def backtracking(n, r, result):
    if not r:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        result.append(i)
        backtracking(n, r-1, result)
        result.pop()

backtracking(N, M, [])