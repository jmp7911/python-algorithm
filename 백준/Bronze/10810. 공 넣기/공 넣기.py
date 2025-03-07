import sys
N,M = map(int, sys.stdin.readline().split())
A = [0 for _ in range(N)]
for _ in range(M):
    i,j,k = map(int, sys.stdin.readline().split())
    A[i-1:j] = [k] * (j-i+1)
print(*A)
