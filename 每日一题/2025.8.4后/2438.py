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
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """预处理前缀积, 时间复杂度 O(U + Q), U 是 n 的二进制表示中 1 的个数"""
        powers = []
        for i in range(31):
            if n & (1 << i):
                powers.append(1 << i)
        
        n = len(powers)
        pre_prod = [1] * (len(powers) + 1)
        for i in range(1, n + 1):
            pre_prod[i] = pre_prod[i - 1] * powers[i - 1]
            
        ans = []
        for l, r in queries:
            ans.append(pre_prod[r + 1] // pre_prod[l] % MOD)
        return ans
    
    # TODO: 逆元
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        for i in range(31):
            if n & (1 << i):
                powers.append(1 << i)
        
        n = len(powers)
        pre_prod = [1] * (len(powers) + 1)
        for i in range(1, n + 1):
            pre_prod[i] = (pre_prod[i - 1] * powers[i - 1]) % MOD

        # 快速幂求模逆元（费马小定理，MOD 是质数）
        def mod_inv(a, mod):
            return pow(a, mod - 2, mod)
            
        ans = []
        for l, r in queries:
            ans.append(pre_prod[r + 1] * mod_inv(pre_prod[l], MOD) % MOD)
        return ans
    
    
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """预处理区间乘积, 空间换时间, 时间复杂度 O(U ** 2 + Q), U 是 n 的二进制表示中 1 的个数"""
        power = []
        for i in range(31):
            if n & (1 << i):
                power.append(1 << i)

        n = len(power)
        pre_prod = [[1] * n for _ in range(n)]
        for i in range(n):
            pre_prod[i][i] = power[i]
            for j in range(i + 1, n):
                pre_prod[i][j] = (pre_prod[i][j - 1] * power[j]) % MOD
        
        ans = []
        for l, r in queries:
            ans.append(pre_prod[l][r])
        return ans
    

MOD = 1_000_000_007
MX = 436
pow2 = [0] * MX   # 预处理 2 的幂, pow2[i] = 2 ** i % MOD
pow2[0] = 1
for i in range(1, MX):
    pow2[i] = pow2[i - 1] * 2 % 1_000_000_007

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        s = [0]
        while n:
            lowbit = n & -n
            e = lowbit.bit_length() - 1
            # 直接计算 e 的前缀和
            s.append(s[-1] + e)
            n ^= lowbit
        return [pow2[s[r + 1] - s[l]] for l, r in queries]