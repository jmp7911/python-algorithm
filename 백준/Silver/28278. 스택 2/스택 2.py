import sys
input = sys.stdin.readline
N = int(input())
stack = dict()
length = 0
top = -1
for _ in range(N):
    x = list(map(int, input().split()))
    if x[0] == 1:
        length += 1
        stack[length] = x[1]
        top = x[1]
    elif x[0] == 2:
        if length > 0:
            print(top)
            length -= 1
            top = stack[length] if length > 0 else -1
        else:
            print(-1)
    elif x[0] == 3:
        print(length)
    elif x[0] == 4:
        if length == 0:
            print(1)
        else:
            print(0)
    elif x[0] == 5:
        if length > 0:
            print(top)
        else:
            print(-1)