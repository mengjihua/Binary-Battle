from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        code_active = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
        
        def judge_code(c):
            if not c:
                return False
            for ch in c:
                if ch not in code_active:
                    return False
            return True
        
        ele, gro, pha, res = [], [], [], []
        for i in range(n):
            if not isActive[i]:
                continue
            
            if not judge_code(code[i]):
                continue
            
            if businessLine[i] == 'electronics':
                ele.append(code[i])
            elif businessLine[i] == 'grocery':
                gro.append(code[i])
            elif businessLine[i] == 'pharmacy':
                pha.append(code[i])
            elif businessLine[i] == 'restaurant':
                res.append(code[i])
        
        return sorted(ele) + sorted(gro) + sorted(pha) + sorted(res)

# if __name__ == '__main__':
#     s = Solution()
#     print(s.validateCoupons(code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [True,True,True,True]))©leetcode