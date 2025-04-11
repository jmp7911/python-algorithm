import sys
input = sys.stdin.readline
N = int(input())
queue = []
length = 0
front = 0
back = -1
for _ in range(N):
    x = input().split()
    if x[0] == 'push':
        length += 1
        queue.append(x[1])
        back = x[1]
    elif x[0] == 'pop':
        if length > 0:
            print(queue[front])
            front += 1
            length -= 1
        else:
            print(-1)
    elif x[0] == 'size':
        print(length)
    elif x[0] == 'empty':
        if length == 0:
            print(1)
        else:
            print(0)
    elif x[0] == 'front':
        if length > 0:
            print(queue[front])
        else:
            print(-1)
    elif x[0] == 'back':
        if length > 0:
            print(back)
        else:
            print(-1)