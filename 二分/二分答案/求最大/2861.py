from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys
sys.setrecursionlimit(10 ** 5 + 1)


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def check(x):
            total_cost = [0] * k
            for i in range(k):
                for j in range(n):
                    total_cost[i] += max(0, (composition[i]
                                         [j] * x - stock[j])) * cost[j]
            print(total_cost)
            return any(cost <= budget for cost in total_cost)
        
        

        l, r = 0, budget // min(cost) + max(stock)
        while l <= r:
            mid = (l + r) // 2
            print(f'l: {l}, r: {r}, mid: {mid}')
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r


if __name__ == '__main__':
    s = Solution()
    # print(s.maxNumberOfAlloys(n=3, k=2, budget=15, composition=[[1, 1, 1], [1, 1, 10]],
    #                           stock=[0, 0, 0], cost=[1, 2, 3]))
    # print(s.maxNumberOfAlloys(n=3, k=2, budget=15, composition=[[1, 1, 1], [1, 1, 10]],
    #                           stock=[0, 0, 100], cost=[1, 2, 3]))
    print(s.maxNumberOfAlloys(n=1, k=7, budget=48, composition=[[1], [5], [9], [6], [4], [2], [4]],
                              stock=[6], cost=[1]))
