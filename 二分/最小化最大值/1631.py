from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    # def minimumEffortPath(self, heights: List[List[int]]) -> int:
    #     n, m = len(heights), len(heights[0])
    #     max_height = max(max(row) for row in heights)
    #     min_height = min(min(row) for row in heights)
                
    #     def check(height_limit):
    #         vis = [[False] * m for _ in range(n)]
    #         vis[0][0] = True
    #         q = deque([(0, 0)])
    #         while q:
    #             x, y = q.popleft()
    #             if x == n - 1 and y == m - 1: return True
    #             for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
    #                 nx, ny = x + dx, y + dy
    #                 if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and abs(heights[nx][ny] - heights[x][y]) <= height_limit:
    #                     vis[nx][ny] = True
    #                     q.append((nx, ny))
    #         return False
        
    #     l, r = 0, max_height - min_height
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if check(mid):
    #             r = mid - 1
    #         else:
    #             l = mid + 1
    #     return l
    
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        cost = [[float('inf')] * m for _ in range(n)]
        cost[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            c, x, y = heappop(heap)
            if x == n - 1 and y == m - 1: return c
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    new_cost = max(c, abs(heights[nx][ny] - heights[x][y]))
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heappush(heap, (new_cost, nx, ny)) 
    
if __name__ == '__main__':
    s = Solution()
    print(s.minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
    print(s.minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]]))