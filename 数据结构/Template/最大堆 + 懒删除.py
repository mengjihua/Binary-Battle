from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class LazyHeap:
    def __init__(self, nums):
        self.heap = []
        self.delayed = defaultdict(int)
        for x in nums:
            heappush(self.heap, -x)
    
    def push(self, x):
        heappush(self.heap, -x)
    
    def remove(self, x):
        self.delayed[-x] += 1
        
    def get_top2(self):
        while self.heap and self.delayed.get(self.heap[0], 0) > 0:
            x = heappop(self.heap)
            self.delayed[x] -= 1
            if self.delayed[x] == 0:
                del self.delayed[x]
        if not self.heap:
            return -10**18, -10**18
        top1 = -self.heap[0]
        x = heappop(self.heap)
        while self.heap and self.delayed.get(self.heap[0], 0) > 0:
            x2 = heappop(self.heap)
            self.delayed[x2] -= 1
            if self.delayed[x2] == 0:
                del self.delayed[x2]
        if not self.heap:
            heappush(self.heap, x)
            return top1, -10**18
        top2 = -self.heap[0]
        heappush(self.heap, x)
        return top1, top2