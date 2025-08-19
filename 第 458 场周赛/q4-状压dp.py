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
    
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        # 构建无向图的邻接表
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        total_states = 1 << n  # 状态压缩，所有节点的子集
        # 三维DP数组：dp[mask][x][y] 表示在mask状态下，以x和y为端点的最长回文路径长度
        dp = [[[-1] * n for _ in range(n)] for _ in range(total_states)]
        ans = 1  # 最小回文路径长度为1（单个节点）

        # 初始化：每个节点自身为长度1的回文路径
        for u in range(n):
            mask = 1 << u
            dp[mask][u][u] = 1

        # 初始化：每条边且两端字符相同，长度为2的回文路径
        for u, v in edges:
            if label[u] == label[v]:
                mask = (1 << u) | (1 << v)
                tu, tv = min(u, v), max(u, v)
                dp[mask][tu][tv] = 2
                ans = 2

        # 状压DP，枚举所有状态
        for mask in range(total_states):
            for x in range(n):
                for y in range(x, n):
                    if dp[mask][x][y] == -1:
                        continue
                    current_len = dp[mask][x][y]
                    ans = max(ans, current_len)
                    # 尝试在x和y两端各扩展一个新节点u和v
                    for u in g[x]:
                        if mask & (1 << u):
                            continue  # u已在路径中
                        for v in g[y]:
                            if u == v or mask & (1 << v) or label[u] != label[v]:
                                continue  # v已在路径中或u,v字符不同或u,v重合
                            new_mask = mask | (1 << u) | (1 << v)
                            new_len = current_len + 2
                            tu, ty = min(u, v), max(u, v)
                            if new_len > dp[new_mask][tu][ty]:
                                dp[new_mask][tu][ty] = new_len
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxLen(n=3, edges=[[0, 1], [1, 2]], label="aba"))
    print(s.maxLen(n=3, edges=[[0, 1], [0, 2]], label="abc"))
    print(s.maxLen(n=4, edges=[[0, 2], [0, 3], [3, 1]], label="bbac"))
    print(s.maxLen(n=5, edges=[[0, 1], [4, 0], [1, 2], [2, 0], [4, 1], [3, 0], [4, 2], [3, 1]], label="stppt"))
    print(s.maxLen(n=7,edges=[[0,1],[1,2],[1,3],[3,4],[0,5],[5,6]],label="aabbcbc"))
