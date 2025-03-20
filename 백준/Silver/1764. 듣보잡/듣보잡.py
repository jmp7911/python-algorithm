import sys
from collections import Counter

input = sys.stdin.readline
N,M=map(int,input().split())
A=[input().strip() for _ in range(N)]
B=[input().strip() for _ in range(M)]
C=Counter(A+B)
answer = []
for name, count in C.items():
    if count==2:
        answer.append(name)
answer.sort()
print(len(answer))
print(*answer, sep='\n')

