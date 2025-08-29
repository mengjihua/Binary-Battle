from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        vis = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        def dfs(x, y):
            res = grid[x][y]
            vis[x][y] = True
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not vis[nx][ny] and grid[nx][ny] >= 1:
                    res += dfs(nx, ny)
                    vis[nx][ny] = True
            
            return res
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] >= 1 and not vis[i][j]:
                    ans += 1 if dfs(i, j) % k == 0 else 0
        return ans
    

if __name__ == '__main__':
    s = Solution()
    print(s.countIslands(grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5))