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
    def minimumBuckets(self, hamsters: str) -> int:
        hamsters = list(hamsters)
        ans, n = 0, len(hamsters)
        for i in range(n):
            if hamsters[i] == 'H':
                if (i - 1 >= 0 and hamsters[i - 1] == 'X') or (i + 1 < n and hamsters[i + 1] == 'X'):
                    continue
                if i + 1 < n and hamsters[i + 1] == '.':
                    ans += 1
                    hamsters[i + 1] = 'X'
                elif i - 1 >= 0 and hamsters[i - 1] == '.':
                    ans += 1
                    hamsters[i - 1] = 'X'
                else:
                    return -1
        return ans
    
    def minimumBuckets(self, hamsters: str) -> int:
        ans, n, idx = 0, len(hamsters), -2
        for i in range(n):
            if hamsters[i] == 'H':
                if idx == i - 1:
                    continue
                if i + 1 < n and hamsters[i + 1] == '.':
                    ans += 1
                    idx = i + 1
                elif i - 1 >= 0 and hamsters[i - 1] == '.':
                    ans += 1
                else:
                    return -1
        return ans
    
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        cnt = i = 0
        while i < n:
            if hamsters[i] != 'H': 
                i += 1
                continue
            if i + 1 < n and hamsters[i + 1] == '.':
                cnt += 1
                i += 3
            elif i - 1 >= 0 and hamsters[i - 1] == '.':
                cnt += 1
                i += 1
            else:
                return -1
        return cnt
    
    def minimumBuckets(self, hamsters: str) -> int:
        if hamsters[:2] == 'HH' or hamsters[-2:] == 'HH' or 'HHH' in hamsters or hamsters == 'H':
            return -1
        replaced = hamsters.replace('H.H', '')
        return (len(hamsters) - len(replaced)) // 3 + replaced.count('H')

if __name__ == "__main__":
    hamsters = Solution()
    print(hamsters.minimumBuckets(".H.H."))
