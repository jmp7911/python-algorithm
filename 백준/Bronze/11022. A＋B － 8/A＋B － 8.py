import sys

T = int(sys.stdin.readline())
for i, item in enumerate(range(T), 1):
    A,B = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')