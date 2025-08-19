from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        matrix = [[-1] * (n + 2)]
        for i in range(m):
            matrix.append([-1] + mat[i] + [-1])
        matrix.append([-1] * (n + 2))
        print(matrix)

        for i in range(1, m + 1):
            l, r = 1, n
            while l <= r:
                mid = (l + r) // 2
                print(i, mid, l, r)
                if matrix[i][mid - 1] < matrix[i][mid] > matrix[i][mid + 1]:
                    break
                elif matrix[i][mid] < matrix[i][mid + 1]:
                    l = mid + 1
                else:
                    r = mid -1 
            print("test", i, mid, l, r)
            if matrix[i][mid] > matrix[i][mid - 1] and matrix[i][mid] > matrix[i][mid + 1] and matrix[i][mid] > matrix[i - 1][mid] and matrix[i][mid] > matrix[i + 1][mid]:
                return [i - 1, mid - 1]
        return [-1, -1]
    
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left, right = 0, len(mat) - 2
        while left <= right:
            mid = (left + right) // 2
            max_num = max(mat[mid])
            idx = mat[mid].index(max_num)
            if max_num > mat[mid + 1][idx]:
                right = mid - 1
            else:
                left = mid + 1
        return [left, mat[left].index(max(mat[left]))]

# Example usage:
mat = [[1,4],[3,2]]
solution = Solution()
# print(solution.findPeakGrid(mat))  # Output: [0, 1]
mat = [[70,50,40,30,20],[100,1,2,3,4]]
print(solution.findPeakGrid(mat))  # Output: [0, 0]