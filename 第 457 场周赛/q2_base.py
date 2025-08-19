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
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        def find_root(x):
            if parent[x] != x:
                parent[x] = find_root(parent[x])
            return parent[x]
        
        def merge(x, y):
            x, y = min(x, y), max(x, y)
            root_x = find_root(x)
            root_y = find_root(y)
            if root_x != root_y:
                parent[root_y] = root_x
        
        connections.sort()
        parent = list(range(c + 1))
        for x, y in connections:
            merge(x, y)
            
        parent_temp = [[] for _ in range(c + 1)]
        for i in range(1, c + 1):
            parent_temp[parent[i]].append(i)
        temp_set = [set(temp) for temp in parent_temp]
        
        print(parent, parent_temp, temp_set)
        
        ans = []
        for op, x in queries:
            if op == 1:
                if not temp_set[parent[x]]:
                    ans.append(-1)
                elif x in temp_set[parent[x]]:
                    ans.append(x)
                else:
                    ans.append(parent_temp[parent[x]][0])
            else:
                if not temp_set[parent[x]]:
                    continue
                parent_temp[parent[x]].remove(x)
                temp_set[parent[x]].remove(x)
            # print(ans, parent_temp, temp_set)
                
        return ans
        

if __name__ == "__main__":
    s = Solution()
    # print(s.processQueries(c = 5, connections = [[1,2],[2,3],[4,3],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]))
    # print(s.processQueries(c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]))
    # print(s.processQueries(c = 1, connections = [], queries = [[1,1],[2,1],[2,1],[2,1],[2,1]]))
    