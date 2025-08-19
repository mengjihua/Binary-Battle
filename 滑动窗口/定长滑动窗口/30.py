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
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        window_len = word_len * len(words)
        target_cnt = Counter(words)
        
        ans = []
        for start in range(word_len):
            window = defaultdict(int)
            temp = 0
            for r in range(start + word_len, len(s) + 1, word_len):
                in_word = s[r - word_len:r]
                window[in_word] += 1
                
                if window[in_word] == target_cnt[in_word]:
                    temp += 1
                
                l = r - window_len
                if l < 0:
                    continue
                if temp == len(target_cnt):
                    ans.append(l)
                
                out_word = s[l:l + word_len]
                window[out_word] -= 1
                if window[out_word] == target_cnt[out_word] - 1:
                    temp -= 1
        return ans

# if __name__ == '__main__':
#     s = Solution()
#     print(s.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
#     print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))