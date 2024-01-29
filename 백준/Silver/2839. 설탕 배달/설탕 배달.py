def solution():
    N = int(input())
    
    answer = -1
    for x in range(N):
        if N < (3*x):
            break
        if (N-(3*x)) % 5 == 0:
            answer = (N-(3*x)) // 5 + x
            break
    return answer
    
print(solution())