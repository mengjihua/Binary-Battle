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

primeSieve = PrimeSieve(999999)
is_prime = primeSieve.is_prime

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        # 八个方向
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        freq = defaultdict(int)
        max_cnt, max_prime = 0, -1
        for i in range(n):
            for j in range(m):
                for dx, dy in directions:
                    temp = 0
                    x, y = i, j
                    while 0 <= x < n and 0 <= y < m:
                        temp = temp * 10 + mat[x][y]
                        if is_prime[temp] and temp > 10:
                            freq[temp] += 1
                            if freq[temp] > max_cnt:
                                max_cnt = freq[temp]
                                max_prime = temp
                            elif freq[temp] == max_cnt and temp > max_prime:
                                max_prime = temp
                        x += dx
                        y += dy
                    
        # print(freq)
        return max_prime


if __name__ == "__main__":
    s = Solution()
    print(s.mostFrequentPrime(mat = [[1,1],[9,9],[1,1]]))
    print(s.mostFrequentPrime([[7]]))