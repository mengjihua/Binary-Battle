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

class Solution:
    # 暴力
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n= len(fruits)
        temp = 0
        
        def remove_smallest_basket(fruit: int) -> bool:
            nonlocal baskets
            for basket in baskets:
                if basket >= fruit:
                    baskets.remove(basket)
                    return True
            return False
        
        for i in range(n):
            if remove_smallest_basket(fruits[i]):
                temp += 1
        return n - temp