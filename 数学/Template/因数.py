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

# 因数分解相关的类
class Factor:
    def __init__(self, max_n=0) -> None:
        """初始化时可预计算max_n范围内的最小质因数表"""
        self.max_n = max(max_n, 1)  # 至少处理到1
        self.min_prime, self.prime_factors = self._build_table(self.max_n)
    
    def _build_table(self, n: int) -> List[int]:
        """构建最小质因数 or 质因数表(0到n)"""
        min_prime = list(range(n + 1))
        prime_factors = [[] for _ in range(n + 1)]
        
        for i in range(2, int(n ** 0.5) + 1):
            if min_prime[i] == i:
                for j in range(i * i, n + 1, i):
                    prime_factors[j].append(i)
                    if min_prime[j] == j:
                        min_prime[j] = i
        return min_prime, prime_factors

    def smallest_prime_factor(self, n: int) -> int:
        """返回n的最小质因数(优化缓存查询)"""
        if n < 1:
            return 0
        if n <= self.max_n:
            return self.min_prime_table[n]
        
        if n % 2 == 0:
            return 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return i
        return n

    def smallest_prime_factors(self, n: int) -> List[int]:
        """返回0到n的最小质因数表(自动扩展缓存)"""
        if n <= self.max_n:
            return self.min_prime_table[:n + 1]
        
        # 扩展缓存
        self.max_n = n
        self.min_prime_table = self._build_spf_table(n)
        return self.min_prime_table[:]

    def max_proper_divisor(self, n: int) -> int:
        """返回n的最大真因数"""
        if n <= 1:
            return 0
        spf = self.smallest_prime_factor(n)
        return 1 if spf == n else n // spf
    
    def prime_factors(self, n: int) -> List[int]:
        """返回n的质因数表"""
        if n < 2:
            return []
        if n <= self.max_n:
            return self.prime_factors[n]
        
        factors = []
        while n > 1:
            spf = self.smallest_prime_factor(n)
            factors.append(spf)
            while n % spf == 0:
                n //= spf
        return factors