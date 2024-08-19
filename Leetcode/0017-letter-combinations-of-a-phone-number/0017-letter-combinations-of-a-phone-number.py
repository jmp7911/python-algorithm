import string
import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        phone = []
        answer = []
        alphabets = string.ascii_lowercase
    
        for digit in digits:
            d = int(digit)
            if d > 7:
                start = (d - 2) * 3 + 1
                if d == 8:
                    end = 3
                else:
                    end = 4
            else:
                start = (d - 2) * 3
                if d == 7:
                    end = 4
                else:
                    end = 3
            
                
                
            phone.append(list(alphabets[start:start+end]))
        
        for x in list(itertools.product(*phone, repeat=1)):
            answer.append(''.join(x))
        return answer