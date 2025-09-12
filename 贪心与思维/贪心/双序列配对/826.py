from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty_profit = sorted(zip(difficulty, profit), key=lambda x: x[0]) 
        pre_max_profit = list(accumulate(
            difficulty_profit, 
            lambda cur_max, next_dp: max(cur_max, next_dp[1]), 
            initial=0))
        # print(difficulty_profit, pre_max_profit)
        
        worker.sort()
        ans, j, n = 0, 0, len(difficulty_profit)
        for w in worker:
            while j < n and difficulty_profit[j][0] <= w:
                j += 1
            if difficulty_profit[j - 1][0] <= w:
                ans += pre_max_profit[j]
        
        return ans
        

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty_profit = sorted(zip(difficulty, profit), key=lambda x: x[0])
        
        worker.sort()
        ans, j, n, max_profit = 0, 0, len(difficulty_profit), 0
        for w in worker:
            while j < n and difficulty_profit[j][0] <= w:
                max_profit = max(max_profit, difficulty_profit[j][1])
                j += 1
            ans += max_profit
        
        return ans

# if __name__ == '__main__':
#     s = Solution()
#     print(s.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]))