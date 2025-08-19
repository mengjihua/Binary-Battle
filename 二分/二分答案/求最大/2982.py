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
    def maximumLength(self, s: str) -> int:
        counter = Counter(s)

        def check(x):
            cnt = [0] * 26
            temp, last_c = 0, ''
            for c in s:
                if last_c != c:
                    last_c = c
                    temp = 1
                else:
                    temp += 1
                if temp == x:
                    cnt[ord(c) - ord('a')] += 1
                    temp = temp - 1
                # print(cnt, temp, last_c)
            return any(cnt[c] >= 3 for c in range(26))

        l, r = 1, max(counter.values()) - 2
        while l <= r:
            mid = (l + r) // 2
            # print(l, r, mid)
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r if check(r) else -1


if __name__ == '__main__':
    s = Solution()
    print(s.maximumLength(s="abcaba"))
