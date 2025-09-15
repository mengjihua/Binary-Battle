from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b
MOD = 10 ** 9 + 7


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        origin = set(wordlist)
        lower_to_origin = {}
        vowel_to_origin = {}
        trans = str.maketrans("aeiou", "?????")  # 替换元音为 '?'

        for s in reversed(wordlist):
            lower = s.lower()
            lower_to_origin[lower] = s
            vowel_to_origin[lower.translate(trans)] = s

        for i, q in enumerate(queries):
            if q in origin:  # 完全匹配
                continue
            lower = q.lower()
            vowel = lower.translate(trans)
            if lower in lower_to_origin:  # 不区分大小写的匹配
                queries[i] = lower_to_origin[lower]
            elif vowel in vowel_to_origin:  # 不区分大小写 + 元音模糊匹配
                queries[i] = vowel_to_origin[vowel]
            else:  # 无匹配
                queries[i] = ""
        return queries