N=int(input())
for i in enumerate(range(2*N-1),1):
    if i[0] // N > 0:
        blank = " " * (i[0] - N)
        star = "*" * (2*N-1 - i[0]%N*2)
    else:
        blank = " " * (N - i[0])
        star = "*" * (2*i[0]-1)
    print(blank + star)
