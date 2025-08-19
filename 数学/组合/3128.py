from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        row_num = [0] * n
        col_num = [0] * m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row_num[i] += 1
                    col_num[i] += 1
        