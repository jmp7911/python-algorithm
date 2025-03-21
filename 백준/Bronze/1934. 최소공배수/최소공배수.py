import sys, math
input = sys.stdin.readline
T=int(input().rstrip())
A=[list(map(int,input().split())) for _ in range(T)]
for x in A:
    print(x[0]*x[1] // math.gcd(*x))