import sys
N=int(sys.stdin.readline())
A=[sys.stdin.readline().split() for _ in range(N)]
A=sorted(A, key=lambda x: int(x[0]))
for i in range(N):
    print(*A[i])