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
setrecursionlimit(2 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

class PrimeSieve:
    def sieve_eratosthenes(self, n: int) -> List[bool]:
        """优化的埃氏筛法，时间复杂度 O(n log log n)"""
        if n < 2:
            return []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        # 只需遍历到 sqrt(n)
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # 从 i*i 开始标记，避免重复标记
                start = i * i
                step = i * 2 if i > 2 else i  # 偶数优化
                is_prime[start::step] = [False] * ((n - start) // step + 1)
        
        return is_prime

    def sieve_euler(self, n: int) -> List[int]:
        if n < 2:
            return []
        is_prime = [i for i in range(n + 1)]
        primes = []
        
        for i in range(2, n + 1):
            if is_prime[i] == i:
                primes.append(i)
            for p in primes:
                if i * p > n:
                    break
                is_prime[i * p] = p
                if i % p == 0:
                    break
        return is_prime

max_n = 10 ** 6 + 1
ps = PrimeSieve()
is_primes = ps.sieve_eratosthenes(max_n)
min_primes = ps.sieve_euler(max_n)
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        indice_mapping = defaultdict(list)
        for idx, x in enumerate(nums):
            if x == 1:
                continue
            temp = x
            factors = set()
            while temp > 1:
                p = min_primes[temp]
                factors.add(p)
                while temp % p == 0:
                    temp //= p
            for p in factors:
                indice_mapping[p].append(idx)
        
        dis = [-1] * n
        dis[0] = 0
        q = deque([0])
        vis = set()
        
        while q:
            i = q.popleft()
            steps = dis[i]
            
            if i == n - 1:
                return steps
            
            if i - 1 >= 0 and dis[i - 1] == -1:
                dis[i - 1] = steps + 1
                q.append(i - 1)
            if i + 1 < n and dis[i + 1] == -1:
                dis[i + 1] = steps + 1
                q.append(i + 1)
                
            x = nums[i]
            if x > 1 and is_primes[x]:
                if x in vis:
                    continue
                vis.add(x)
                for j in indice_mapping[x]:
                    if j == i:
                        continue
                    if dis[j] == -1:
                        dis[j] = steps + 1
                        q.append(j)
                        
        return dis[n - 1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.minJumps(nums = [1,2,4,6]))
    print(s.minJumps(nums = [2,3,4,7,9]))
    print(s.minJumps(nums = [4,6,5,8]))