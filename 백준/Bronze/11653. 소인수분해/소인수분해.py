M = int(input())
if M == 1:
    pass
else:
    while M > 1:
        for i in range(2, M+1):
            if M % i == 0:
                print(i)
                M = M // i
                break
        if i == M - 1:
            print(M)
            break