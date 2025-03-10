N, B = map(int, input().split())

# B의 i승 으로 나눈 나머지를 구한다
# 11진수부터는 알파벳으로 변환한다

i = 1
answer = ""
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while N >= B**(i-1):
    digit = N % B**i // B**(i-1)
    answer = digits[digit] + answer
    i += 1
print(answer)

