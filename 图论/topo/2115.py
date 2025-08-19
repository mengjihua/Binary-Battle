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
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        g = defaultdict(list)
        indegree = defaultdict(int)
        for v, us in zip(recipes, ingredients):
            for u in us:
                g[u].append(v)
                indegree[v] += 1
        
        q = deque(supplies)
        while q:
            u = q.popleft()
            if u not in g: continue
            for v in g[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
                    
        # ans = []
        # while q:
        #     u = q.popleft()
        #     if u not in g: continue
        #     for v in g[u]:
        #         indegree[v] -= 1
        #         if indegree[v] == 0:
        #             q.append(v)
        #             ans.append(v)
                    
        # return ans
                    
        return [v for v in recipes if indegree[v] == 0]