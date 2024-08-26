class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "":0, "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
        }
        sumv = dic[s[-1]]
        s = s[::-1]
        for i, x in enumerate(s):
            if i + 1 == len(s):
                break
            print(dic[s[i+1]], sumv)
            if dic[s[i+1]] < sumv and dic[s[i+1]] < dic[s[i]]:
                sumv -= dic[s[i+1]]
            else:
                sumv += dic[s[i+1]]
        
        return sumv
            
                
