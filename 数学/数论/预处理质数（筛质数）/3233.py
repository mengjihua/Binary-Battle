from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class PrimeSieve:
    def __init__(self, max_n=0):
        """初始化时可预计算max_n范围内的素数表"""
        self.max_n = max_n
        self.is_prime, self.primes = self.sieve_eratosthenes(max_n) 

    def sieve_eratosthenes(self, n: int) -> List[int]:
        """埃氏筛法，时间复杂度 O(n log log n)"""
        if n < 2:
            return [False] * (n + 1), []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime, [i for i in range(n + 1) if is_prime[i]]

    def sieve_euler(self, n: int) -> List[int]:
        """欧拉筛法（线性筛），时间复杂度 O(n)"""
        if n < 2:
            return []
        is_prime = [True] * (n + 1)
        primes = []
        is_prime[0] = is_prime[1] = False

        for i in range(2, n + 1):
            if is_prime[i]:
                primes.append(i)
            for p in primes:
                if i * p > n:
                    break
                is_prime[i * p] = False
                if i % p == 0:
                    break
        return primes
    
    def judge_prime(self, n: int) -> bool:
        """判断一个数是否为素数, 时间复杂度 O(√n)"""
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return n >= 2

# print(pow(10 ** 9, 1 / 2))  # 31622.776601683792
ps = PrimeSieve(31622)
primes = ps.primes

temp = []
for p in primes:
    temp.append(p * p)

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        l_bound, r_bound = bisect_left(temp, l), bisect_left(temp, r + 1)
        # print(temp[l_bound:r_bound])
        return r - l + 1 - (r_bound - l_bound)
    

if __name__ == "__main__":
    s = Solution()
    print(s.nonSpecialCount(l = 4, r = 16))