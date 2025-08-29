from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                subgrid = [grid[x][j:j + k] for x in range(i, i + k)]
                
                elements = []
                for row in subgrid:
                    elements.extend(row)
                elements.sort()
                
                min_diff = float('inf')
                for x in range(1, len(elements)):
                    if elements[x] == elements[x - 1]:
                        continue
                    min_diff = min(min_diff, elements[x] - elements[x - 1])
                ans[i][j] = min_diff if min_diff != float('inf') else 0
                
        return ans

# [[1,8],[3,-2]]
# 2
# [[3,-1]]
# 1
# [[1,-2,3],[2,3,5]]
# 2
# 测试
s = Solution()
# print(s.minAbsDiff([[1,8],[3,-2]], 2))
# print(s.minAbsDiff([[3,-1]], 1))
print(s.minAbsDiff([[1,-2,3],[2,3,5]], 2))