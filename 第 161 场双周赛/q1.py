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

class Prime:
    def __init__(self, n=0) -> None:
        self.n = n
        self.prime = []
        self.is_prime = [True] * (n + 1)

    # 埃拉托斯特尼筛法 (Sieve of Eratosthenes)
    def sieve_of_eratosthenes(n):
        primes = []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, n + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return primes

    # 修改, 埃拉托斯特尼筛法 (Sieve of Eratosthenes)
    def sieve_of_eratosthenes(self, n):
        primes = []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        for i in range(int(n ** 0.5) + 1, n + 1):
            if is_prime[i]:
                primes.append(i)
        return primes

    # 欧拉筛(线性筛)
    def euler_sieve(n):
        prime = []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, n + 1):
            if is_prime[i]:
                prime.append(i)
            for j in prime:
                if i * j > n:
                    break
                is_prime[i * j] = False
                if i % j == 0:
                    break
        return prime


prime = Prime()
is_prime = set(prime.sieve_of_eratosthenes(10 ** 5 + 1))

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        sum_A = 0
        sum_B = 0
        for i in range(n):
            if i in is_prime:
                sum_A += nums[i]
            else:
                sum_B += nums[i]
        
        return abs(sum_A - sum_B)