import sys

N, S = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
answer = 0 if sum(arr) < S else N
if not answer:
    print(answer)
    sys.exit()
sumarr = [0 for _ in range(N)]
left, right = (0, 0)

while left <= right:
    sumarr[right] = sumarr[right - 1] + arr[right - 1]
    if sumarr[right] - sumarr[left] + arr[right] >= S:
        answer = min(answer, right - left + 1)
        left += 1
    else:
        if right == N - 1:
            left += 1
        else:
            right += 1

    
print(answer)