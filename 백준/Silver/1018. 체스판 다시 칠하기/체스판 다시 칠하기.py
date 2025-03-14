N,M = map(int, input().split())
C = [[s for s in input()] for _ in range(N)]

WB = ['W','B']
answer = 64
for i in range(N-7):
    for j in range(M-7):
        count1 = 0
        count2 = 0
        for k in range(i,i+8):
            for l in range(j, j+8):
                if C[k][l] != WB[(k+l) % 2]:
                    count1 += 1
                elif C[k][l] == WB[(k+l) % 2]:
                    count2 += 1
        answer = min(count1, count2, answer)
print(answer)