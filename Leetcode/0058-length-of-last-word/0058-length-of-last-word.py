class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        for x in l[::-1]:
            if x != '':
                return len(x)
        return 1