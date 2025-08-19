from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        ans, n = 0, len(fruits)
        for i in range(n):
            ans += fruits[i][i]
            fruits[i][i] = 0
            
        directions = [[[1, -1], [1, 0], [1, 1]], [[-1, 1], [0, 1], [1, 1]]]
        
        @lru_cache(maxsize=None)
        def dfs(i, j, opt):
            if opt == 0 and i > j:
                return -inf # 不可能到达
            if opt == 1 and i < j:
                return -inf # 不可能到达
            if i == n - 1 and j == n - 1:
                return 0 # 到达终点
            
            res = 0
            for dx, dy in directions[opt]:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n:
                    res = _max(res, dfs(x, y, opt))
            return res + fruits[i][j]
        
        return ans + dfs(0, n - 1, 0) + dfs(n - 1, 0, 1)

if __name__ == '__main__':
    s = Solution()
    print(s.maxCollectedFruits(fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]))