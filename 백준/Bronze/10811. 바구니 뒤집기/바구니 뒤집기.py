N,M=map(int,input().split())
A=[i for i in range(N+1)]
for _ in range(M):
    i,j = map(int,input().split())
    A[i:j+1] = A[i:j+1][::-1]
print(*A[1:])