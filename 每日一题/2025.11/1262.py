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

class Solution:
    # def maxSumDivThree(self, nums: List[int]) -> int:
    #     one, two, three = [], [], []
    #     for num in nums:
    #         if num % 3 == 1:
    #             one.append(num)
    #         elif num % 3 == 2:
    #             two.append(num)
    #         else:
    #             three.append(num)
    #     one.sort(reverse=True), two.sort(reverse=True), three.sort(reverse=True)
        
    #     ans, p = sum(three), 0
    #     n, m = len(one), len(two)
    #     while p < n and p < m:
    #         ans += one[p] + two[p]
    #         p += 1
        
        
    #     # if n - p >= 3:
    #     #     a = (n - p) // 3
    #     #     ans += sum(one[p:p + a * 3])
    #     #     p += a * 3
    #     # if n - p == 2:
    #     #     if n >= 3 and m >= 1:
    #     #         return max(ans, ans - two[-1] + one[p] + one[p + 1])
    #     # elif n - p == 1:
    #     #     if n >= 3 and m >= 2:
    #     #         return max(ans, ans - two[-1] - two[-2] + one[p])
        
    #     # if m - p >= 3:
    #     #     a = (m - p) // 3
    #     #     ans += sum(two[p:p + a * 3])
    #     #     p += a * 3
    #     # if m - p == 2:
    #     #     if m >= 3 and n >= 1:
    #     #         return max(ans, ans - one[-1] + two[p] + two[p + 1])
    #     # elif m - p == 1:
    #     #     if m >= 3 and n >= 2:
    #     #         return max(ans, ans - one[-1] - one[-2] + two[p])
        
    #     # return ans
        
    #     def solve(length1, length2, lst1, lst2, idx, ans):
    #         res = ans
    #         if length1 - idx >= 3:
    #             a = (length1 - idx) // 3
    #             res = max(res, res + sum(lst1[idx:idx + a * 3]))
    #             idx += a * 3
    #         if length1 - idx == 2:
    #             if length1 >= 3 and length2 >= 1:
    #                 return max(res, res - lst2[-1] + lst1[idx] + lst1[idx + 1])
    #         elif length1 - idx == 1:
    #             if length1 >= 3 and length2 >= 2:
    #                 return max(res, res - lst2[-1] - lst2[-2] + lst1[idx])
    #         return res
    #     return max(solve(n, m, one, two, p, ans), solve(m, n, two, one, p, ans))
 
    # def maxSumDivThree(self, nums: List[int]) -> int:
    #     s = sum(nums)
    #     if s % 3 == 0:
    #         return s
    #     a1 = sorted(x for x in nums if x % 3 == 1)
    #     a2 = sorted(x for x in nums if x % 3 == 2)
    #     if s % 3 == 2:
    #         a1, a2 = a2, a1
    #     ans = s - a1[0] if a1 else 0
    #     if len(a2) > 1:
    #         ans = max(ans, s - a2[0] - a2[1])
    #     return ans
    
    
    def maxSumDivThree(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, mod):
            if i < 0:
                return float('-inf') if mod != 0 else 0
            return max(dfs(i - 1, mod), dfs(i - 1, (mod + nums[i]) % 3) + nums[i])
        return dfs(len(nums) - 1, 0)

if __name__ == '__main__':
    s = Solution()
    print(s.maxSumDivThree([13,21,7,27,40,18,37,7,31,5]))