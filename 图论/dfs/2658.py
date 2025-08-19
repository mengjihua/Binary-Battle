from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def bfs(x, y):
            stack = [(x, y)]
            vis[x][y] = True
            fish_num = 0
            
            while stack:
                tx, ty = stack.pop()
                fish_num += grid[tx][ty]
                for dx, dy in directions:
                    nx, ny = tx + dx, ty + dy
                    if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny] and grid[nx][ny] != 0:
                        vis[nx][ny] = True
                        stack.append((nx, ny))
            return fish_num
            
        
        vis = [[False] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and not vis[i][j]:
                    ans = max(ans, (bfs(i, j)))
        return ans

    def findMaxFish1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            res = grid[i][j]
            grid[i][j] = 0
            for dx, dy in directions:
                x, y = dx + i, dy + j
                res += dfs(x, y)
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))
        return ans

# 测试
if __name__ == '__main__':
    s = Solution()
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
    print(s.findMaxFish(grid))