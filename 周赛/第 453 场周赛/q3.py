from typing import List
from collections import deque


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        dp = [0] * (n + 1)
        s = [0] * (n + 1)
        dp[0] = 1
        s[0] = 1
        
        minQ = deque()
        maxQ = deque()
        l = 0
        
        for r in range(n):
            while minQ and nums[minQ[-1]] > nums[r]:
                minQ.pop()
            minQ.append(r)
            
            while maxQ and nums[maxQ[-1]] < nums[r]:
                maxQ.pop()
            maxQ.append(r)
            
            while minQ and maxQ and nums[maxQ[0]] - nums[minQ[0]] > k:
                if minQ[0] == l:
                    minQ.popleft()
                if maxQ[0] == l:
                    maxQ.popleft()
                l += 1
            
            if l == 0:
                dp[r + 1] = s[r] % MOD
            else:
                dp[r + 1] = (s[r] - s[l - 1]) % MOD
            
            s[r + 1] = (s[r] + dp[r + 1]) % MOD
        
        return dp[n] % MOD

# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.countPartitions([9,4,1,3,7] , 4))  # Example test case
    print(s.countPartitions([3, 3, 4], 0))
    
    # print(s.countPartitions([1, 2, 3], 1))      # Another test case
    # print(s.countPartitions([5, 6, 7], 3))      # Yet another test case
    # print(s.countPartitions([1, 2, 3, 4, 5], 0))  # Edge case with k = 0