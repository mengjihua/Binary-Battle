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
    # def maxDistance(self, arrays: List[List[int]]) -> int:
    #     max_nums = [(idx, arr[-1]) for idx, arr in enumerate(arrays)]
    #     min_nums = [(idx, arr[0]) for idx, arr in enumerate(arrays)]
    #     max_nums.sort(key=lambda x: x[1]), min_nums.sort(key=lambda x: x[1])
        
    #     max_idx1, max_num1, max_num2 = max_nums[-1][0], max_nums[-1][1], max_nums[-2][1]
    #     min_idx1, min_num1, min_num2 = min_nums[0][0], min_nums[0][1], min_nums[1][1]
        
    #     if max_idx1 != min_idx1:
    #         return max_num1 - min_num1
    #     else:
    #         return max(max_num1 - min_num2, max_num2 - min_num1)
    
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        min_num, max_num = inf, -inf
        for arr in arrays:
            ans = max(ans, max_num - arr[0], arr[-1] - min_num)
            min_num = min(min_num, arr[0])
            max_num = max(max_num, arr[-1])
        return ans
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxDistance([[1,2,3],[4,5],[1,2,3]]))