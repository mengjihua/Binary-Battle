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
    # def possibleStringCount(self, word: str) -> int:
        # combination = []
        # temp = ''
        # for c in word:
        #     if temp:
        #         if c == temp[0]:
        #             temp += c
        #         else:
        #             combination.append(temp)
        #             temp = c
        #     else:
        #         temp = c
        # combination.append(temp)
        
        # ans = set()
        # def dfs(depth: int, going: bool, path: List[str]) -> None:
        #     if depth == len(combination):
        #         ans.add(''.join(path))
        #         return

        #     if going:
        #         dfs(depth + 1, True, path + [combination[depth]])
        #     else:
        #         dfs(depth + 1, False, path + [combination[depth]])
        #         tt = ''
        #         for c in combination[depth]:
        #             tt += c
        #             dfs(depth + 1, True, path + [tt])
            
        # dfs(0, False, [])
        # # print(ans)
        # return len(ans)
        
    def possibleStringCount(self, word: str) -> int:
        # count_str = Counter(word)
        # ans = 1
        # for cnt in count_str.values():
        #     ans += cnt - 1
        # return ans
        last_c = ''
        for c in word:
            if c == last_c:
                ans += 1
            else:
                last_c = c
        return ans

# if __name__ == '__main__':
#     word = "abbcccc"
#     print(Solution().possibleStringCount(word))