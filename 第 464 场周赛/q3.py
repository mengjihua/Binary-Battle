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

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.size = 1
        while self.size < size:
            self.size *= 2
        self.data = [0] * (2 * self.size)
    
    def update(self, index, value):
        i = index + self.size
        self.data[i] = value
        i //= 2
        while i:
            self.data[i] = max(self.data[2 * i], self.data[2 * i + 1])
            i //= 2
            
    def query(self, l, r):
        if l > r:
            return 0
        l += self.size
        r += self.size
        res = 0
        while l <= r:
            if l % 2 == 1:
                res = max(res, self.data[l])
                l += 1
            if r % 2 == 0:
                res = max(res, self.data[r])
                r -= 1
            l //= 2
            r //= 2
        return res

from collections import deque

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    graph[i].append(j)
            for j in range(i):
                if nums[j] > nums[i]:
                    graph[i].append(j)
        
        ans = [0] * n
        for i in range(n):
            visited = [False] * n
            queue = deque([i])
            visited[i] = True
            max_val = nums[i]
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        max_val = max(max_val, nums[neighbor])
                        queue.append(neighbor)
            ans[i] = max_val
        
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maxValue(nums = [2,1,3]))
    print(s.maxValue(nums = [2,3,1]))