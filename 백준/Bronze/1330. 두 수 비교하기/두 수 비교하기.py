import sys

N,M = map(int, sys.stdin.readline().split())

if N > M:
    print('>')
elif N < M:
    print('<')
else:
    print('==')