from functools import lru_cache
# https://leetcode.cn/problems/beautiful-arrangement/

class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache(None)
        def dfs(idx, state):
            if idx > n:
                return 1
            res = 0
            for i in range(1, n + 1):
                if state >> (i - 1) & 1 == 0 and (i % idx == 0 or idx % i == 0):
                    res += dfs(idx + 1, state | (1 << (i - 1)))
            return res
        return dfs(1, 0)
    
    def countArrangement2(self, n: int) -> int:
        dp = [0] * (1 << n + 1)
        dp[0] = 1
        for state in range(1 << n):
            idx = bin(state).count('1') + 1
            for i in range(1, n + 1):
                # print(f'state: {state}, idx: {idx}, i: {i}, dp: {dp}, state >> (i - 1) & 1: {state >> (i - 1) & 1}')
                if state >> (i - 1) & 1 == 0 and (i % idx == 0 or idx % i == 0):
                    dp[state | (1 << (i - 1))] += dp[state]
        # print(dp)        
        return max(dp)
        
# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.countArrangement2(1))
    print(s.countArrangement2(2))
# print(0 | (1 << 1))