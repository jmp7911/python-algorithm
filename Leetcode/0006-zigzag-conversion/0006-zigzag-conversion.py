class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = ""
        
        if numRows == 1:
            answer = s
        else:
            cycle = 2 + (numRows - 2) * 2
            zigzag = ["" for _ in range(numRows)]
            for i, c in enumerate(s):
                if i % cycle >= numRows:
                    zigzag[cycle - (i % cycle)] += c
                else:
                    zigzag[i % cycle] += c
            for x in zigzag:
                answer += x
        return answer
