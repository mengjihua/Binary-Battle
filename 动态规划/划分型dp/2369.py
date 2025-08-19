from typing import List
from functools import lru_cache
from functools import cache

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def dfs(depth):
            if depth == n:
                return True
            elif depth == n - 1:
                return False
            
            if nums[depth] == nums[depth + 1]:
                if depth + 2 < n and nums[depth] == nums[depth + 2]:
                    return dfs(depth + 2) or dfs(depth + 3)
                return dfs(depth + 2)
            elif nums[depth] + 1 == nums[depth + 1] and depth + 2 < n and nums[depth] + 2 == nums[depth + 2]:
                return dfs(depth + 3)
            
            return False
        return dfs(0)