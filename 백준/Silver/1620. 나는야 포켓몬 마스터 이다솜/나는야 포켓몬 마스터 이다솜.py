import sys
N,M=map(int,sys.stdin.readline().split())
d_number = {}
d_alpha = {}
for i in range(N):
    name = sys.stdin.readline().strip()
    d_number[i+1] = name
    d_alpha[name] = i+1
B=[sys.stdin.readline().strip() for _ in range(M)]
for x in B:
    if x.isalpha():
        print(d_alpha[x])
    elif x.isnumeric():
        print(d_number[int(x)])