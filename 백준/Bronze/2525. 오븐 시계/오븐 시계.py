import sys

H,M = map(int, sys.stdin.readline().split())
A = int(sys.stdin.readline())

minutes = H*60 + M + A

minutes %= 1440

print(minutes//60, minutes%60)