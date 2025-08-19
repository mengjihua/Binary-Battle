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
    def separateSquares(self, squares: List[List[int]]) -> float:
        sum_area = 0
        min_y, max_y = float('inf'), float('-inf')
        for x, y, side_length in squares:
            sum_area += side_length ** 2
            min_y = min(min_y, y + side_length / 2)
            max_y = max(max_y, y + side_length / 2)
        
        def check(limit_y):
            half_area = 0
            for x, y, side_length in squares:
                if y < limit_y:
                    half_area += side_length * min(limit_y - y, side_length)
            return half_area >= sum_area / 2
        
        while abs(max_y - min_y) > 1e-5:
            mid_y = (min_y + max_y) / 2
            # print(f"mid_y: {mid_y}, min_y: {min_y}, max_y: {max_y}")
            if check(mid_y):
                max_y = mid_y
            else:
                min_y = mid_y
        return max_y

if __name__ == '__main__':
    s = Solution()
    print(s.separateSquares(squares = [[0,0,1],[2,2,1]]))