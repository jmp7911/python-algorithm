class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        answer = True
        opened = ["(", "{", "["]
        closed = [")", "}", "]"]
        dic = {
            ")":"(", "}":"{", "]":"["
        }
        for b in s:
            if b in opened:
                stack.append(b)
            elif b in closed:
                if len(stack) > 0:
                    if stack[-1] == dic[b]:
                        stack.pop()
                    else:
                        answer = False
                        break
                else:
                    answer = False
                    break
        if len(stack) > 0:
            answer = False
        
        return answer