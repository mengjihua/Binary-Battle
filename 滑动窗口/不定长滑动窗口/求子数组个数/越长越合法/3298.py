from typing import List
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
    def validSubstringCount(self, word1: str, word2: str) -> int:
        target_cnt = Counter(word2)
        sum_cnt = Counter(word1)
        if any(sum_cnt[c] < target_cnt[c] for c in target_cnt):
            return 0
        
        ans = r = 0
        cnt, temp_cnt = len(target_cnt), 0
        window = defaultdict(int)
        for l in range(len(word1)):
            while r < len(word1) and temp_cnt < cnt:
                window[word1[r]] += 1
                if word1[r] in target_cnt and window[word1[r]] == target_cnt[word1[r]]:
                    temp_cnt += 1
                r += 1
            if temp_cnt == cnt:
                ans += len(word1) - r + 1
            if word1[l] in target_cnt and window[word1[l]] == target_cnt[word1[l]]:
                temp_cnt -= 1
            window[word1[l]] -= 1
                
        return ans

# if __name__ == '__main__':
#     s = Solution()
#     print(s.validSubstringCount(word1 = "bcca", word2 = "abc"))
#     print(s.validSubstringCount(word1 = "abcabc", word2 = "abc"))