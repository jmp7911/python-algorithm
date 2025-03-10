N, B = input().split()
B = int(B)
result = 0
for index, i in enumerate(N[::-1]):
    if i.isalpha():
        i = ord(i) - 55
    else:
        i = int(i)
    result += i * B ** index
print(result)