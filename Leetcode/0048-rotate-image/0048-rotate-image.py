from collections import deque
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i, x in enumerate(list(zip(*matrix[::-1]))):
            matrix[i] = x
