import sys
N,M = map(int, sys.stdin.readline().split())
A = [i for i in range(N+1)]
for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
print(*A[1:])