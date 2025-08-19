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

# 因数分解相关的类
class Factor:
    def __init__(self, max_n=0) -> None:
        """初始化时可预计算max_n范围内的最小质因数表"""
        self.max_n = max(max_n, 1)  # 至少处理到1
        self.min_prime_table = self._build_spf_table(self.max_n)
    
    def _build_spf_table(self, n: int) -> List[int]:
        """构建最小质因数表(0到n)"""
        min_prime = list(range(n + 1))
        min_prime[1] = 1
        
        for i in range(2, int(n ** 0.5) + 1):
            if min_prime[i] == i:
                for j in range(i * i, n + 1, i):
                    if min_prime[j] == j:
                        min_prime[j] = i
        return min_prime

    def smallest_prime_factor(self, n: int) -> int:
        """返回n的最小质因数(优化缓存查询)"""
        if n < 1:
            return 0
        if n <= self.max_n:
            return self.min_prime_table[n]
        
        if n % 2 == 0:
            return 2
        for i in range(3, int(n**0.5) + 1, 2):
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


factor = Factor()
n_min_primes = factor.smallest_prime_factors(10 ** 6)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        for i in range(n - 1, 0, -1):
            if nums[i] >= nums[i - 1]:
                continue
            if nums[i] < nums[i - 1]:
                max_proper_divisor = factor.max_proper_divisor(nums[i - 1])
                nums[i - 1] //= max_proper_divisor
                if nums[i] < nums[i - 1]:
                    return -1
                ans += 1
        return ans
    
    def minOperations(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        for i in range(n - 1, 0, -1):
            if nums[i] >= nums[i - 1]:
                continue
            if nums[i] < nums[i - 1]:
                nums[i - 1] = n_min_primes[nums[i - 1]]
                if nums[i] < nums[i - 1]:
                    return -1
                ans += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    start = timestamp()
    print(s.minOperations(nums=[994009] * (10 ** 5 - 1) + [997]))
    end = timestamp()
    print(f'耗时: {end - start:.6f} 秒')
    # factor = Factor()
    # max_num, max_min_factor = 1, 1
    # for i in range(1, 10 ** 6 + 1):
    #     min_factor = factor.smallest_prime_factor(i)
    #     if min_factor > max_min_factor and min_factor != i:
    #         max_num, max_min_factor = i, min_factor
    # print(f'1 到 10^6 中最小质因数最大的数是: {max_num}, 最小质因数是: {max_min_factor}')
