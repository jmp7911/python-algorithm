import sys
N,M=map(int,sys.stdin.readline().split())
d = dict()
A=[sys.stdin.readline() for _ in range(N)]
B=[sys.stdin.readline() for _ in range(M)]
for x in A:
    d[x] = 1
cnt = 0
for x in B:
    try:
        cnt += d[x]
    except:
        pass
print(cnt)