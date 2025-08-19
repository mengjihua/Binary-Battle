from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = [[False] * n for _ in range(m)]
        # border = [[False] * n for _ in range(m)], 这种方法进行染色需要 O(n * m) 的时间复杂度和空间复杂度
        # 直接使用列表存储边界坐标
        border = []
        
        def dfs(i, j):
            vis[i][j] = True
            
            for dx, dy in directions:
                x, y = dx + i, dy + j
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == grid[i][j] and not vis[x][y]:
                        dfs(x, y)
                    elif grid[x][y] != grid[i][j]:
                        border.append((i, j))
                else:
                    border.append((i, j))
        dfs(row, col)
        
        # print(border)
        for r, c in border:
            grid[r][c] = color
        return grid
    
# 测试
if __name__ == '__main__':
    s = Solution()
    grid = [[1, 2, 2], [2, 3, 2]]
    row, col, color = 0, 1, 3
    result = s.colorBorder(grid, row, col, color)
    for row in result:
        print(row)