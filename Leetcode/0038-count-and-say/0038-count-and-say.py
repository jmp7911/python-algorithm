class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        print(s, n)
        if len(s) == 1:
            return "1" + s
        else:
            be = ""
            l = 0
            result = ""
            for i in range(len(s)):
                if be == "":
                    be = s[i]
                    l = 1
                elif be == s[i]:
                    l += 1
                else:
                    result += str(l) + be
                    be = s[i]
                    l = 1
            return result + str(l) + be