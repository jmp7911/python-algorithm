import sys
N=int(sys.stdin.readline())
A=[tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
A = sorted(A, key=lambda x: (x[1], x[0]))
for a in A:
    print(*a)