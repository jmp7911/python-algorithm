white = [[0]*101 for _ in range(101)]

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            white[x+i][y+j] = 1
print(sum(sum(row) for row in white))