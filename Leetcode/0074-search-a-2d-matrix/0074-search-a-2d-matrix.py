class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        last = [matrix[i][-1] for i in range(n)]
        row = bisect_left(last, target)
        if row == n:
            return False
        col = bisect_left(matrix[row], target)
        
        return True if matrix[row][col] == target else False
