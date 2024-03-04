#자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

import sys
N, M = map(int, sys.stdin.readline().split())

def backtracking(n, r, result, visited):
    if not r:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backtracking(n, r-1, result, visited)
            visited[i] = False
            result.pop()
visited = [False]*(N+1)
backtracking(N, M, [], visited)