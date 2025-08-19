from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            row, col = divmod(mid, len(matrix[0])) # divmod()函数返回两个值，分别是除数和余数
            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
    