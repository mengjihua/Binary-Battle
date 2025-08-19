from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        ans = []
        cur_sum = 2
        # while finalSum == cur_sum or finalSum > cur_sum * 2:
        #     ans.append(cur_sum)
        #     finalSum -= cur_sum
        #     cur_sum += 2
        # return ans + [finalSum] if finalSum > 0 else ans
        while cur_sum <= finalSum:
            ans.append(cur_sum)
            finalSum -= cur_sum
            cur_sum += 2
        ans[-1] += finalSum
        return ans