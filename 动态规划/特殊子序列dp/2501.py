from typing import List
from functools import lru_cache

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ans, nums = 0, set(nums)
        
        for num in nums:
            cnt = 1
            while num ** 2 in nums:
                num **= 2
                cnt += 1
            ans = max(ans, cnt)
        return ans if ans > 1 else -1
    
    def longestSquareStreak2(self, nums: List[int]) -> int:
        nums = set(nums)
        
        @lru_cache(maxsize=None)
        def dfs(num):
            if num not in nums:
                return 0
            return dfs(num ** 2) + 1
        
        ans = max(dfs(num) for num in nums)
        return ans if ans > 1 else -1
        
                
                
    
# 测试
if __name__ == '__main__':
    nums = [4,3,6,16,1,8,2]
    print(Solution().longestSquareStreak(nums))