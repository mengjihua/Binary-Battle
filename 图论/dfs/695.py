from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        vis = [[False] * m for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(x, y):
            vis[x][y] = True
            res = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and grid[nx][ny] == 1:
                    res += dfs(nx, ny)
            return res
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans            