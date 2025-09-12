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
    def removeAlmostEqualCharacters(self, word: str) -> int:
        ans, n, p = 0, len(word), 1
        while p < n:
            if abs(ord(word[p - 1]) - ord(word[p])) <= 1:
                ans += 1
                p += 2
            else:
                p += 1
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.removeAlmostEqualCharacters(word = "aaaaa"))
    print(s.removeAlmostEqualCharacters(word = "acba"))
    # print(s.removeAlmostEqualCharacters('aaa'))
    # print(s.removeAlmostEqualCharacters('abcde'))
    # print(s.removeAlmostEqualCharacters('aabbcc'))