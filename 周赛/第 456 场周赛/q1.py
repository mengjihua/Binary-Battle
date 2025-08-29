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
    def partitionString(self, s: str) -> List[str]:
        ans = []
        temp = set()
        tt = ''
        for c in s:
            tt += c
            if tt not in temp:
                ans.append(tt)
                temp.add(tt)
                tt = ''
        return ans

if __name__ == '__main__':
    s = Solution()
    s = 'a' * (10 ** 5)
    # 计算函数执行时间
    start_time = datetime.now()
    ans = s.partitionString(s)
    end_time = datetime.now()
    print(ans)