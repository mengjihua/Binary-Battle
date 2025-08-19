from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from string import ascii_lowercase
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    # def kthCharacter(self, k: int, operations: List[int]) -> str:
    #     if not operations:
    #         return 'a'

    #     op = operations.pop()
    #     n = 1 << len(operations)
    #     if k <= n:
    #         return self.kthCharacter(k, operations)
        
    #     ans = self.kthCharacter(k - n, operations)
    #     return ascii_lowercase[(ord(ans) - ord('a') + op) % 26]
    
    # def kthCharacter(self, k: int, operations: List[int]) -> str:
    #     def dfs(k, operations) -> int:
    #         if not operations:
    #             return 0

    #         op = operations.pop()
    #         n = 1 << len(operations)
    #         if k <= n:
    #             return dfs(k, operations)
            
    #         ans = dfs(k - n, operations)
    #         return (ans + op) % 26
        
    #     return ascii_lowercase[dfs(k, operations)]
    
    # def kthCharacter(self, k: int, operations: List[int]) -> str:
    #     n = (k - 1).bit_length()
    #     # if k == 1:
    #     #     return 'a'
    #     # n = floor(log(k - 1, 2)) + 1
    #     temp = 0
    #     for i in range(n - 1, -1, -1):
    #         if k > (1 << i):
    #             k -= (1 << i)
    #             temp += operations[i]
    #     return ascii_lowercase[temp % 26]
    
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        n = k.bit_length()
        inc =  sum([op for i, op in enumerate(operations[:n]) if (k >> i) & 1])
        return ascii_lowercase[inc % 26]