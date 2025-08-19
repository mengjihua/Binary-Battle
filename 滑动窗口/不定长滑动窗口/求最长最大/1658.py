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
    def minOperations(self, nums: List[int], x: int) -> int:
        n, sum_nums = len(nums), sum(nums)
        if sum_nums < x:
            return -1
        if sum_nums == x:
            return n
        
        temp, r = 0, n
        while r > 0 and temp < x:
            r -= 1
            temp += nums[r]
        ans = n - r if temp == x else float('inf')
            
        for l in range(n):
            temp += nums[l]
            while r < n and temp > x:
                temp -= nums[r]
                r += 1
            ans = min(ans, n - r + l + 1) if temp == x else ans
            # print(l, r, ans)
        return ans if ans != float('inf') else -1
    
    
    def minOperations(self, nums: List[int], x: int) -> int:
        n= len(nums)
        
        temp, r = 0, n
        while r > 0 and temp < x:
            r -= 1
            temp += nums[r]
        ans = n - r if temp == x else float('inf')
            
        for l in range(n):
            temp += nums[l]
            while r <= l or (r < n and temp > x):
                temp -= nums[r]
                r += 1
            ans = min(ans, n - r + l + 1) if temp == x else ans
            # print(l, r, ans)
        return ans if ans != float('inf') else -1
    
# if __name__ == "__main__":
#     print(Solution().minOperations(nums = [1,1,4,2,3], x = 5))