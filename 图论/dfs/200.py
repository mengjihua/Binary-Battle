from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(x, y):
            visited[x][y] = True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1' and not visited[nx][ny]:
                    dfs(nx, ny)
        
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    cnt += 1
                    dfs(i, j)
        return cnt

# 测试
if __name__ == '__main__':
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    print(Solution().numIslands(grid))  # 输出: 1
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    print(Solution().numIslands(grid))  # 输出: 3