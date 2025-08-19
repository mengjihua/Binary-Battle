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
    def isValid(self, word: str) -> bool:
        if len(word) <= 2:
            return False
        
        judge = [False] * 2
        for c in word:
            if c.isalpha():
                if c in 'aeiouAEIOU':
                    judge[0] = True
                else:
                    judge[1] = True
            elif c.isdigit():
                continue
            else:
                return False
        return all(judge)
                