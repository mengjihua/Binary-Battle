from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) + 1 <= 0: return -1
        
        heap = []
        sm = 1
        regret_cnt = 0
        for num in nums:
            sm += num
            if num < 0: heappush(heap, num)
            while heap and sm <= 0:
                sm -= heappop(heap)
                regret_cnt += 1
        return regret_cnt
    
if __name__ == '__main__':
    s = Solution()
    print(s.magicTower(nums = [100,100,100,-250,-60,-140,-50,-50,100,150]))
    print(s.magicTower(nums = [-200,-300,400,0]))