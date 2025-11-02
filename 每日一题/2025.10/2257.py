from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate, pairwise
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, comb, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # valid[x][y][direction]: 表示 (x,y) 朝 direction 方向是否可达 | 未曾被监视
        valid = [[[True] * 4 for _ in range(n)] for _ in range(m)]
        for x, y in walls:
            for d in range(4):
                valid[x][y][d] = False
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(x, y, d):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if valid[x][y][d]:
                valid[x][y][d] = False
                dfs(x + directions[d][0], y + directions[d][1], d)
            
        for x, y in guards:
            for d in range(4):
                valid[x][y][d] = False
                dfs(x + directions[d][0], y + directions[d][1], d)
            
        # ans = 0
        # for i in range(m):
        #     for j in range(n):
        #         if all(valid[i][j]):
        #             ans += 1
        # return ans
        return sum(1 for i in range(m) for j in range(n) if all(valid[i][j]))

if __name__ == "__main__":
    s = Solution()
    print(s.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]))