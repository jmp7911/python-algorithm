class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digit = 1
        n1, n2 = 0, 0
        for i, s in enumerate(num1[::-1]):
            n1 += (ord(s) - ord('0')) * digit
            digit *= 10
        digit = 1
        for i, s in enumerate(num2[::-1]):
            n2 += (ord(s) - ord('0')) * digit
            digit *= 10
        
        return str(n1 * n2)
        