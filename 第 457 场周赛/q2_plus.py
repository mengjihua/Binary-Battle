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


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))
        rank = [0] * (c + 1)

        def find_root(x):
            if parent[x] != x:
                parent[x] = find_root(parent[x])
            return parent[x]

        def merge(x, y):
            rx, ry = find_root(x), find_root(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
                
        for x, y in connections:
            merge(x, y)

        comp_dict = defaultdict(list)
        for i in range(1, c + 1):
            root = find_root(i)
            comp_dict[root].append(i)

        comp_heaps = {}
        for root, nodes in comp_dict.items():
            heapify(nodes)
            comp_heaps[root] = nodes

        print(parent, comp_dict, comp_heaps)
        
        is_valid = [True] * (c + 1)
        ans = []
        for op, x in queries:
            if op == 2:
                is_valid[x] = False
            else:
                if is_valid[x]:
                    ans.append(x)
                else:
                    root = find_root(x)
                    heap = comp_heaps[root]
                    while heap and not is_valid[heap[0]]:
                        heappop(heap)
                    if heap:
                        ans.append(heap[0])
                    else:
                        ans.append(-1)
        return ans

if __name__ == "__main__":
    s = Solution()
    # print(s.processQueries(c = 5, connections = [[1,2],[2,3],[4,3],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]))
    # print(s.processQueries(c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]))
    # print(s.processQueries(c = 1, connections = [], queries = [[1,1],[2,1],[2,1],[2,1],[2,1]]))
    print(s.processQueries(c = 4, connections = [[3,4],[4,2]], 
                           queries = [[1,1],[2,3],[2,2],[2,1],[1,1],[2,2],[1,1],[2,1],
                                      [1,4],[1,3],[2,3],[2,4],[1,3],[1,3],[1,3],[1,4],
                                      [2,2],[2,3],[1,2],[2,3],[1,3],[2,3],[2,3],[2,4],
                                      [1,3],[2,4],[2,2],[1,3],[2,1],[1,1],[1,1],[1,4],
                                      [2,2],[1,2],[1,4],[1,1],[2,1],[1,3],[2,3],[1,1]]))
