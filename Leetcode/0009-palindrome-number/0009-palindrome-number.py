class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        tostring = str(x)
        if x == int(tostring[::-1]):
            return True
        else:
            return False