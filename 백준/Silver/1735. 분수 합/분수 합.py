import math, sys
input = sys.stdin.readline
A,B=map(int, input().split())
C,D=map(int, input().split())
son = A*D+B*C
mom = B*D
gcd = math.gcd(son,mom)
print(son//gcd, mom//gcd)