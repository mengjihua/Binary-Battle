from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 6 + 1)

class Solution:
    # 超出时间按限制
    # def hasAllCodes(self, s: str, k: int) -> bool:
    #     for i in range(2 ** k):
    #         bi_num = bin(i)[2:].zfill(k)
    #         if bi_num not in s:
    #             return False
    #     return True

    # def hasAllCodes2(self, s: str, k: int) -> bool:
    #     set_judge = set()
    #     for i in range(len(s) - k + 1):
    #         set_judge.add(s[i:i + k])
    #     return len(set_judge) == 2 ** k
    
    # def hasAllCodes3(self, s: str, k: int) -> bool:
    #     return len(set(s[i:i + k] for i in range(len(s) - k + 1))) == 2 ** k
    
    # 滚动哈希
    def hasAllCodes4(self, s: str, k: int) -> bool:
        if len(s) < (1 << k) + k - 1:
            return False
        
        num = int(s[:k], base=2)
        exists = set([num])

        for i in range(1, len(s) - k + 1):
            num = (num - ((ord(s[i - 1]) - 48) << (k - 1))) * 2 + (ord(s[i + k - 1]) - 48)
            exists.add(num)
        
        return len(exists) == (1 << k)