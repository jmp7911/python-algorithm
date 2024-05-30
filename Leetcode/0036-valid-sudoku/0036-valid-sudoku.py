class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # is valid each row
        for rows in board:
            digits = []
            for col in rows:
                if col != '.' and col in digits:
                    return False
                digits.append(col)
        # is valid each column
        for col in range(9):
            digits = []
            for row in range(9):
                if board[row][col] != '.' and board[row][col] in digits:
                    return False
                digits.append(board[row][col])
        # is valid each sub-box
        x, y = (0, 0)
        while x < 9 and y < 9:
            digits = []
            for i in range(3):
                for j in range(3):
                    d = board[i+x][j+y]
                    if d != '.' and d in digits:
                        return False
                    digits.append(d)
            y = (y + 3) % 9
            if y == 0:
                x += 3
        for rows in board:
            digits = []
            for col in rows:
                digits.append(col)
            print(digits)
        return True