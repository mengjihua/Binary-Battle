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
MOD = 10 ** 9 + 7

class Solution:
    # 记忆化搜索 + DFS
    # def checkPowersOfThree(self, n: int) -> bool:
    #     mx_limit = int(log(n, 3)) + 1
    #     @lru_cache(maxsize=None)
    #     def dfs(i, cur):
    #         if cur == n:
    #             return True
    #         if cur > n or i > mx_limit:
    #             return False
    #         return dfs(i + 1, cur + 3 ** i) or dfs(i + 1, cur)  # or: 短路
    #     return dfs(0, 0)
    
    # 优化内存, BFS
    def checkPowersOfThree(self, n: int) -> bool:
        mx_limit = int(log(n, 3)) + 1
        q = deque([(0, 0)])
        while q:
            i, cur = q.popleft()
            if cur == n:
                return True
            if cur > n or i > mx_limit:
                continue
            q.append((i + 1, cur + 3 ** i))
            q.append((i + 1, cur))
        return False
    
    # 三进制
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2:
                return False
            n //= 3
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkPowersOfThree(91))