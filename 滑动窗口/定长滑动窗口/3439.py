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
# https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-i/

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n, sqare_time, ans = len(startTime), 0, 0
        for i in range(n + 1):
            sqare_time += (startTime[i] if i < n else eventTime) - (endTime[i - 1] if i > 0 else 0)
            if i < k:
                continue
            ans = max(ans, sqare_time)
            # TODO 发题解, 右边减数之前忘加括号, 导致错误
            # 忘加括号会导致在 i < k 时, 计算 sqare_time 时减去 0 而不是 (startTime[i - k] - 0)
            sqare_time -= startTime[i - k] - (endTime[i - k - 1] if i - k - 1 >= 0 else 0)
        
        return ans
    
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n, sqare_time, ans = len(startTime), 0, 0
        startTime, endTime = startTime + [eventTime], [0] + endTime
        for i in range(n + 1):
            sqare_time += startTime[i] - endTime[i]
            if i < k:
                continue
            ans = max(ans, sqare_time)
            sqare_time -= startTime[i - k] - endTime[i - k]
        
        return ans

# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.maxFreeTime(5, 1, [1, 3], [2, 5]))
    print(s.maxFreeTime(eventTime = 21, k = 1, startTime = [7,10,16], endTime = [10,14,18]))