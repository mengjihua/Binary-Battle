from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate, pairwise
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, comb, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional['TreeNode']) -> int:
        
        def get_sm(node):
            if not node:
                return 0
            return node.val + get_sm(node.left) + get_sm(node.right)
        
        sm = get_sm(root)
        
        res = 0
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            lsm = dfs(node.left)
            rsm = dfs(node.right)
            
            if node.left:
                res = max(res, lsm * (sm - lsm))
            if node.right:
                res = max(res, rsm * (sm - rsm))
            
            return node.val + lsm + rsm
        
        dfs(root)
        
        return res % MOD