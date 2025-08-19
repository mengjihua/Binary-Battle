from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        cnt = list(Counter(nums).values())
        
        def isPrime(n):
            vis = [False] * (n + 1)
            primes = []
            for i in range(2, n + 1):
                if not vis[i]:
                    primes.append(i)
                    vis[i] = True
                for prime in primes:
                    if i * prime > n: break
                    vis[i * prime] = True
                    if i % prime == 0: break
            return primes
        
        prime = set(isPrime(max(cnt)))
        for c in cnt:
            if c in prime:
                return True
        return False