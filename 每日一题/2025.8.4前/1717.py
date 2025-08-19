from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    # def maximumGain(self, s: str, x: int, y: int) -> int:
    #     if x < y:
    #         s = s.replace('a', '1').replace('b', '2').replace('1', 'b').replace('2', 'a')
    #         x, y = y, x
    #     # print(s, x, y)
    #     stack = []
    #     ans = 0
    #     for c in s:
    #         if not stack and c != 'a' and c != 'b':
    #             continue
    #         if c == 'a':
    #             stack.append(c)
    #         elif c == 'b':
    #             if stack and stack[-1] == 'a':
    #                 stack.pop()
    #                 ans += x
    #             else:
    #                 stack.append(c)
    #         else:
    #             stack.append(c)
                
    #     stack2 = []
    #     for c in stack:
    #         if not stack2 and c != 'a' and c != 'b':
    #             continue
    #         if c == 'b':
    #             stack2.append(c)
    #         elif c == 'a':
    #             if stack2 and stack2[-1] == 'b':
    #                 stack2.pop()
    #                 ans += y
    #             else:
    #                 stack2.append(c)
    #         else:
    #             stack2.append(c)

    #     return ans
    
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s.replace('a', '1').replace('b', '2').replace('1', 'b').replace('2', 'a')
            x, y = y, x
        # print(s, x, y)
        stack = []
        ans = 0
        for c in s:
            if not stack and c != 'a' and c != 'b':
                continue
            if stack and stack[-1] == 'a' and c == 'b':
                stack.pop()
                ans += x
            else:
                stack.append(c)
                
        stack2 = []
        for c in stack:
            if not stack2 and c != 'a' and c != 'b':
                continue
            if stack2 and stack2[-1] == 'b' and c == 'a':
                stack2.pop()
                ans += y
            else:
                stack2.append(c)

        return ans

    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = "a", "b"
        if x < y:
            x, y = y, x
            a, b = b, a
        ans = cnt1 = cnt2 = 0
        for c in s:
            if c == a:
                cnt1 += 1
            elif c == b:
                if cnt1:
                    ans += x
                    cnt1 -= 1
                else:
                    cnt2 += 1
            else:
                ans += min(cnt1, cnt2) * y
                cnt1 = cnt2 = 0
        ans += min(cnt1, cnt2) * y
        return ans
    

if __name__ == '__main__':
    s = Solution()
    print(s.maximumGain(s = "cdbcbbaaabab", x = 4, y = 5))