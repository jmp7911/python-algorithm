import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
S = list(sorted(set(A), key=lambda x: x))
d = dict()
for i, x in enumerate(S):
    d[x] = i
for a in A:
    print(d[a], end=' ')