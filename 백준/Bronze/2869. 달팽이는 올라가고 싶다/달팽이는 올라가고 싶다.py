import math
A, B, V = map(int, input().split())

if V == A:
    print(1)
else:
    print(math.ceil((V - A) / (A - B)) + 1)
