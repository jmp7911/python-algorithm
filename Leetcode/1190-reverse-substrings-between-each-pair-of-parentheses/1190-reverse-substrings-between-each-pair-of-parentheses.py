class Solution:
    def reverseParentheses(self, s: str) -> str:
        answer = ""

        stack = []
        brackets = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                start = stack.pop()
                brackets.append((start, i))
            
        arr = list(s)
        for s, e in brackets:
            arr[s+1:e] = arr[e-1:s:-1]
        
        mytable = str.maketrans("", "", "()")
            
        return "".join(arr).translate(mytable)