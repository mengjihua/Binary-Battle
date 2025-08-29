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
        chars = sorted(label)
        char_range = {}
        for i, c in enumerate(chars):
            char_range[c] = (char_range.get(c, 0) | (1 << i))
        color = [0] * (1 << n)
        single_range_approx = [0] * (1 << n)
        for state in range(1, 1 << n):
            lowbit = (state & -state)
            last_color = color[state ^ lowbit]
            last_value = single_range_approx[state ^ lowbit]
            mask = char_range[label[lowbit.bit_length() - 1]]
            last_bits = (last_color & mask)
            valid_bits = last_bits ^ mask
            color[state] = last_color | (valid_bits & (-valid_bits))
            if last_bits.bit_count() % 2:
                last_value += 2
            single_range_approx[state] = last_value
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        connectivity = [None] * (1 << n)
        for state in range(1 << n):
            visited = [bool((1 << i) & state) for i in range(n)]
            counter = [None] * n
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    q = [i]
                    f = 0
                    while f < len(q):
                        x = q[f]
                        f += 1
                        for v in graph[x]:
                            if not visited[v]:
                                visited[v] = True
                                q.append(v)
                    state2 = sum((1 << j) for j in q)
                    for j in q:
                        counter[j] = (i, state2)
            connectivity[state] = counter
        def approx(state, start, end):
            i1, c1 = connectivity[state][start]
            i2, c2 = connectivity[state][end]
            if i1 != i2:
                return state.bit_count() + (color[c1] & color[c2]).bit_count() * 2
            elif start == end:
                return state.bit_count() + 1 + single_range_approx[c1 ^ (1 << start)]
            else:
                return state.bit_count() + single_range_approx[c1]
        state_conv = [[None] * n for _ in range(n)]
        for start in range(n):
            for end in range(start, n):
                if label[start] == label[end]:
                    conv_l = {}
                    for v1 in graph[start]:
                        for v2 in graph[end]:
                            if v1 != v2 and label[v1] == label[v2]:
                                conv_l.setdefault(v1, []).append(v2)
                    state_conv[start][end] = list(conv_l.items())

        visited = set()
        qs = [[] for _ in range(n + 1)]
        for i in range(n):
            approx_result = approx(0, i, i)
            v = ((1 << i), i, i)
            visited.add(v)
            qs[approx_result].append(v)
        for i in range(n):
            for j in graph[i]:
                if i < j and label[i] == label[j]:
                    approx_result = approx(0, i, j)
                    v = ((1 << i) | (1 << j), i, j)
                    visited.add(v)
                    qs[approx_result].append(v)
        ans = 0
        for i in range(n, -1, -1):
            q = qs[i]
            while q:
                state, start, end = q.pop()
                ans = max(ans, state.bit_count())
                if ans >= i:
                    return ans
                for v1, v2l in state_conv[start][end]:
                    if not ((1 << v1) & state):
                        mid_state = (state, v1, end)
                        if mid_state in visited:
                            continue
                        visited.add(mid_state)
                        for v2 in v2l:
                            if not ((1 << v2) & state):
                                v1a, v2a = sorted([v1, v2])
                                next_ = (state | (1 << v1a) | (1 << v2a), v1a, v2a)
                                if next_ not in visited:
                                    visited.add(next_)
                                    qs[approx(state, v1a, v2a)].append(next_)
        return ans