from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b
MOD = 10 ** 9 + 7

def rotate(a: List[List[int]]) -> List[List[int]]:
    return list(zip(*reversed(a)))

class Solution:
    def solve(self, a: List[List[int]]) -> int:
        # 限定在 a 的 [l,r) 列中
        def minimumArea(grid: List[List[int]], limit_l: int, limit_r: int) -> int:
            n = len(grid)
            def get1():
                for j in range(limit_l, limit_r):
                    for i in range(n):
                        if grid[i][j] == 1:
                            return j
                return inf
            def get2():
                for j in range(limit_r - 1, limit_l - 1, -1):
                    for i in range(n):
                        if grid[i][j] == 1:
                            return j
                return -inf
            def get11():
                for i in range(n):
                    for j in range(limit_l, limit_r):
                        if grid[i][j] == 1:
                            return i
                return inf
            def get22():
                for i in range(n - 1, -1, -1):
                    for j in range(limit_l, limit_r):
                        if grid[i][j] == 1:
                            return i
                return -inf
            l, r = get1(), get2()
            hi, lo = get11(), get22()
            
            return (lo - hi + 1) * (r - l + 1)
        
        ans = inf
        m, n = len(a), len(a[0])
        
        if m >= 3:
            for i in range(1, m):
                for j in range(i + 1, m):
                    area = minimumArea(a[:i], 0, n)
                    area += minimumArea(a[i:j], 0, n)
                    area += minimumArea(a[j:], 0, n)
                    ans = _min(ans, area)

        if m >= 2 and n >= 2:
            for i in range(1, m):
                for j in range(1, n):
                    area = minimumArea(a[:i], 0, n)
                    area += minimumArea(a[i:], 0, j)
                    area += minimumArea(a[i:], j, n)
                    ans = _min(ans, area)

                    # 图片上右
                    area = minimumArea(a[:i], 0, j)
                    area += minimumArea(a[:i], j, n)
                    area += minimumArea(a[i:], 0, n)
                    ans = _min(ans, area)
                    
        return ans

    def minimumSum(self, grid: List[List[int]]) -> int:
        return min(self.solve(grid), self.solve(rotate(grid)))

if __name__ == '__main__':
    s = Solution()
    print(s.minimumSum([[1,0,1,0],[0,1,0,1]]))