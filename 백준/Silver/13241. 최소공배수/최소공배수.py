import sys,math
input = sys.stdin.readline
A,B=map(int, input().split())
gcd = math.gcd(A,B)
print(A*B//gcd)