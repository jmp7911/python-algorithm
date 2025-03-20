import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
B=list(map(int,sys.stdin.readline().split()))
d={}
for x in A:
    d[x] = d.get(x, 0) + 1
answer = []
for y in B:
    try:
        answer.append(d[y])
    except:
        answer.append(0)
print(*answer)