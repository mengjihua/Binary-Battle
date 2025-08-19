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

from 质数 import PrimeSieve

def test_performance():
    """测试两种筛法的性能"""
    test_sizes = [1_000_000, 5_000_000, 10_000_000]
    prime_sieve = PrimeSieve()
    for n in test_sizes:
        print(f"\n测试范围: 1-{n:,}")
        
        # 测试埃氏筛
        start = timestamp()
        _, primes_eratosthenes = prime_sieve.sieve_eratosthenes(n)
        eratosthenes_time = timestamp() - start
        print(f"埃氏筛 - 耗时: {eratosthenes_time:.4f}秒, 素数数量: {len(primes_eratosthenes):,}")

        # 测试欧拉筛
        start = timestamp()
        primes_euler = prime_sieve.sieve_euler(n)
        euler_time = timestamp() - start
        print(f"欧拉筛 - 耗时: {euler_time:.4f}秒, 素数数量: {len(primes_euler):,}")

        # 验证结果一致性
        assert primes_eratosthenes == primes_euler, "两种算法结果不一致！"
        print("结果验证: 一致")

if __name__ == "__main__":
    test_performance()