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
def input(): return stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b
MOD = 10 ** 9 + 7

# TODO: 递归调用次数过多，可能会导致超时
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        cnt = 0
        @lru_cache(None)
        def dfs(i, n):
            nonlocal cnt
            if n == 0:
                return 1
            upper = int(n ** (1 / x)) + 1
            res = 0
            for j in range(i + 1, upper + 1):
                cnt += 1
                if n - j ** x >= 0:
                    res += dfs(j, n - j ** x)
                else:
                    break
            return res
        res = dfs(0, n)
        print(f'枚举次数: {cnt}')
        return res % MOD

    def numberOfWays(self, n: int, x: int) -> int:
        cnt = 0
        @lru_cache(None)
        def dfs(i, n):
            nonlocal cnt
            cnt += 1
            if n == 0:
                return 1
            if n - i ** x < 0:
                return 0
            return dfs(i + 1, n) + dfs(i + 1, n - i ** x)
        res = dfs(1, n)
        print(f'枚举次数: {cnt}')
        return res % MOD


if __name__ == '__main__':
    s = Solution()
    start = timestamp()
    s.numberOfWays(20, 1)
    end = timestamp()
    print(f'用时: {end - start}')