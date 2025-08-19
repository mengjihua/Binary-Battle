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
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans, l = 0 ,0
        window = defaultdict(int)
        for r in range(len(answerKey)):
            window[answerKey[r]] += 1
            while min(window['T'], window['F']) > k:
                window[answerKey[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans