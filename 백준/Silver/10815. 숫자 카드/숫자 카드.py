import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
B=list(map(int,sys.stdin.readline().split()))
d = dict()
for i in A:
    d[i] = 1
answer = []
for i in B:
    try:
        answer.append(d[i])
    except:
        answer.append(0)
print(*answer)