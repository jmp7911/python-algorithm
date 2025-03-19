import sys
N,M=map(int,sys.stdin.readline().split())
A=[sys.stdin.readline() for _ in range(N)]
B=[sys.stdin.readline() for _ in range(M)]
print(len(list(filter(lambda x: x in A, B))))