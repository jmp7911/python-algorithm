class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = ["(", ")"]
        ans = []
        answer = []
        def isValid(s):
            stack = []
            answer = True
            for x in s:
                if x == "(":
                    stack.append(x)
                else:
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        answer = False
                        break
            if len(stack) > 0:
                answer = False
            return answer

        def backtracking():
            if len(ans) == n*2:
                if isValid(ans):
                    answer.append("".join(ans))
                return
            for x in l:
                ans.append(x)
                print(ans)
                backtracking()
                
                ans.pop()
        
        backtracking()

        return answer

    


    