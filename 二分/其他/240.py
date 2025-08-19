from typing import List
from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        # i, j = 0, m - 1
        # while i < n and j >= 0:
        #     if matrix[i][j] == target:
        #         return True
        #     elif matrix[i][j] > target:
        #         j -= 1
        #     else:
        #         i += 1
        # return False
        
        for row in matrix:
            idx = bisect_left(row, target)
            if idx < m and row[idx] == target:
                return True
        return False
  