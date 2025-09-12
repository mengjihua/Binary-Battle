from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    # def minOperations(self, n: int) -> int:
    #     ans = inf
    #     def dfs(cur_val, depth):
    #         nonlocal ans
    #         if depth > ans:
    #             return
    #         if cur_val == 0:
    #             ans = min(ans, depth)
    #         else:
    #             pow1, pow2 = ceil(log(cur_val, 2)), floor(log(cur_val, 2))
    #             dfs(abs(cur_val - 2 ** pow1), depth + 1)
    #             dfs(abs(cur_val - 2 ** pow2), depth + 1)
    #     dfs(n, 0)
    #     return ans
    
    def minOperations(self, n: int) -> int:
        max_op_cnt = bin(n).count('1')
        @lru_cache(maxsize=None)
        def dfs(cur_val, depth):
            if depth > max_op_cnt:
                return inf
            if cur_val == 0:
                return depth
            else:
                pow1, pow2 = ceil(log(cur_val, 2)), floor(log(cur_val, 2))
                return min(
                    dfs(abs(cur_val - 2 ** pow1), depth + 1), 
                    dfs(abs(cur_val - 2 ** pow2), depth + 1)
                )
        return dfs(n, 0)
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.minOperations(n = 39))
    print(s.minOperations(n = 54))